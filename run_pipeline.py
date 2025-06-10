from pathlib import Path

from extract.read_csv import read_csv

if __name__ == "__main__":
    input_path = Path("InformeConsumos_Mayo.csv")

    df = read_csv(input_path)

    print(df.head())
   
    