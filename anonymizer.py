
from pathlib import Path
import pandas as pd

def reader(file: Path) -> pd.DataFrame:
    """
    Reads a CSV file using UTF-8 encoding and ';' as separator.
    Drops any row where the first column (e.g., 'supplier') is NaN.

    Parameters:
        file (Path): Path to the CSV file.

    Returns:
        pd.DataFrame: Raw dataframe.
    """
    try:
        df = pd.read_csv(file, encoding="utf-8", sep=";")
        # Drop rows where the first column (supplier) is NaN
        df = df.dropna(subset=[df.columns[0]])
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to read the file {file}: {e}")


def cleaner(df: pd.DataFrame) -> pd.DataFrame:
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
    df.iloc[:, 0] = df.iloc[:, 0].astype(str).str.strip().str.title()

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

    print(df.head())  # Preview of cleaned data
    return df


if __name__ == "__main__":
    path_to_file = Path("report_may2025.csv")
    raw_df = reader(path_to_file)
    cleaned_df = cleaner(raw_df)