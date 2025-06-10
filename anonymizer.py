
from pathlib import Path
import pandas as pd
import re



def read_report (file: Path) -> pd.DataFrame:
    """
    Reads the raw spanish original report and convert to utg"""
    try:
        df = pd.read_csv(file, encoding="latin-1", sep=";")
        # Drop rows where the first column (supplier) is NaN
        df = df.dropna(subset=[df.columns[0]])
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to read the file {file}: {e}")

