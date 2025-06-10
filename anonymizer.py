
from pathlib import Path
import pandas as pd
import re



def read_and_decode (file: Path) -> pd.DataFrame:
    """
    Reads the raw spanish original report and convert to utf-8
    """

    try:
        df = pd.read_csv(file, encoding="latin-1", sep=";")
        print(df.head())
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to read the file {file}: {e}")
    

if __name__ == "__main__":

    file_path = Path('InformeConsumos_Mayo.csv')
    report = read_and_decode(file_path)



# Drop rows where the first column (supplier) is NaN
# # df = df.dropna(subset=[df.columns[0]])