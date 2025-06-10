
import pandas as pd
import re

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drops columns at index 3 and 6 (e.g., "encargos")
    Rename columns, translating from Spanish to English


    Returns a cleaned DataFrame.
    """
    # Drops non useful columns.
    df = df.drop(columns=[df.columns[3], df.columns[6]], errors="ignore")
    # Rename columns before further transformations
    df = df.rename(columns={
        "PROVEEDOR": "supplier",
        "Acum. Almacén 2025": "warehouse_2025",
        "Acum. Directo 2025": "direct_2025",
        "Acum. Almacén 2024": "warehouse_2024",
        "Acum. Directo 2024": "direct_2024"
    })
    # Removes spaces and converts column names to lowercase
    df.columns = df.columns.str.strip().str.lower()

    # Removes spaces and converts to lowercase 'supplier' column
    df.iloc[:, 0] = df.iloc[:, 0].astype(str).str.strip().str.lower()
    
    # Removes strange characters and spaces
    df.iloc[:, 0] = df.iloc[:, 0].str.replace(r"[^a-z0-9]", "", regex=True)

    # Replaces "," with "." in all numeric values
    for col in df.columns[1:]:
        df[col] = pd.to_numeric(
        df[col].astype(str).str.replace(",", ".", regex=False).str.strip(),
        errors="coerce"
    )
        
    # Replace NaNs in numeric columns with 0
    df[df.columns[1:]] = df[df.columns[1:]].fillna(0)
    
    return df