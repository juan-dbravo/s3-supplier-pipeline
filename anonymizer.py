
import pandas as pd

def cleaner(file: str) -> pd.DataFrame:
    """Reads a CSV file encoded in Latin-1, skipping the first row and using ';' as separator."""
    try:
        df = pd.read_csv(file, encoding="latin-1", sep=";", skiprows=1)
        print(df.head())  # For preview
    
        for column_name in df.columns[1:]:  # Skip the first column (e.g., 'supplier')
            values = df[column_name]  # Get the column values
            values = values.str.replace(",", ".")  # Replace commas with dots
            values = values.astype(float, errors='ignore')  # Convert to float if possible
            df[column_name] = values  # Store back into the DataFrame
                

    except Exception as e:
        raise RuntimeError(f"Failed to read the file: {e}")

if __name__ == "__main__":
    cleaner("report_may2025.csv")