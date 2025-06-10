
import pandas as pd

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drops columns at index 3 and 6 (e.g., "encargos").
    Returns a cleaned DataFrame.
    """
    df = df.drop(columns=[df.columns[3], df.columns[6]], errors="ignore")
    return df