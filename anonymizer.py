
from pathlib import Path
import pandas as pd
import re

def read_report (file: Path) -> pd.DataFrame:
    """
    Reads a CSV file using UTF-8 encoding and ';' as separator.
    Drops any row where the first column (e.g., 'supplier') is NaN.

    Parameters:
        file (Path): Path to the CSV file.

    Returns:
        pd.DataFrame: Raw dataframe.
    """
    try:
        df = pd.read_csv(file, encoding="latin-1", sep=";")
        # Drop rows where the first column (supplier) is NaN
        df = df.dropna(subset=[df.columns[0]])
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to read the file {file}: {e}")


def clean_report (df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the supplier report dataframe:
    - Standardizes supplier names
    - Converts number formats
    - Replaces NaNs in numeric columns with 0

    Parameters:
        df (pd.DataFrame): Raw dataframe

    Returns:
        pd.DataFrame: Cleaned dataframe
    """

    # Clean the first column (supplier names)
    df.iloc[:, 0] = df.iloc[:, 0].astype(str).str.strip().str.lower()

    # Clean numeric columns
    for col in df.columns[1:]:
        df[col] = pd.to_numeric(
            df[col]
            .astype(str)
            .str.replace(",", ".", regex=False)
            .str.strip(),
            errors="coerce"
        )

    # Replace NaNs in numeric columns with 0
    df[df.columns[1:]] = df[df.columns[1:]].fillna(0)

    return df

def normalize_name(name: str) -> str:
    # Remove punctuation and spaces, keep only a–z, 0–9
    name = re.sub(r"[^a-z0-9]", "", name)
    return name

def anonymize_report(df : pd.DataFrame) -> pd.DataFrame:

    supplier_col =  df.columns[0]
    df["__supplier_key__"] = df[supplier_col].apply(normalize_name)

    representative = (
        df[[supplier_col, "__supplier_key__"]]
        .drop_duplicates()
        .groupby("__supplier_key__")
        .first()[supplier_col]

    )
    # Map normalized key → anonymized name
    mapping = {
        key: f"Supplier_{str(i+1).zfill(3)}"
        for i, key in enumerate(sorted(representative.index))
    }

    # Replace original names with anonymized values
    df[supplier_col] = df["__supplier_key__"].map(mapping)

    # Drop helper column
    df.drop(columns="__supplier_key__", inplace=True)

    return df



if __name__ == "__main__":
    path_to_file = Path("report_feb2025.csv")
    raw_df = read_report(path_to_file)
    print(raw_df.head())
    clean_df = clean_report(raw_df)
    print(clean_df.head())
    anonymized_df = anonymize_report(clean_df)
    print(anonymized_df.head())
