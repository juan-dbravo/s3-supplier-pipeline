
from pathlib import Path
import pandas as pd


def read_csv (file: Path) -> pd.DataFrame:
    """
    Reads the raw spanish original report and convert to utf-8
    """

    try:
        df = pd.read_csv(file, encoding="latin-1", sep=";")
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to read the file {file}: {e}")
    
