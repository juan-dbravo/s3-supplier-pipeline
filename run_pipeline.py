from pathlib import Path
import pandas as pd

from extract.read_csv import read_csv
from transform.clean_df import clean_df

if __name__ == "__main__":
    input_path = Path("InformeConsumos_Mayo.csv")

    raw_df = read_csv(input_path)
    cleaned_df = clean_df(raw_df)

    print(cleaned_df.head())
   
    cleaned_df.to_csv("example.csv", index=False, encoding="utf-8")