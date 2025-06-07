
import pandas as pd

def cleaner(file: str) -> pd.DataFrame:
    """Reads a CSV file encoded in Latin-1, skipping the first row and using ';' as separator."""
    try:
        df = pd.read_csv(file, encoding="utf-8", sep=";")
        df = df.drop(index=0).reset_index(drop=True)

        # Clean the first column (supplier names)
        df.iloc[:, 0] = df.iloc[:, 0].astype(str).str.strip().str.title()
    
        for col in df.columns[1:]:  # Skip the first column (e.g., 'supplier')
            values = df[col]  # Get the column values
            values = values.str.replace(",", ".")  # Replace commas with dots
            values = values.astype(float, errors='ignore')  # Convert to float if possible
            df[col] = values  # Store back into the DataFrame

        # Replace NaNs in numeric columns with 0
        df[df.columns[1:]] = df[df.columns[1:]].fillna(0)
                
        print(df.head())  # For preview

    except Exception as e:
        raise RuntimeError(f"Failed to read the file: {e}")

if __name__ == "__main__":
    cleaner("report_may2025.csv")