import pandas as pd
from pathlib import Path

DATA_PATH = Path("../data/raw")

print("=" * 50)
print("DATA QUALITY AUDIT")
print("=" * 50)

csv_files = list(DATA_PATH.glob("*.csv"))

if not csv_files:
    print("No CSV files found. Check your DATA_PATH.")
else:2
    for file in csv_files:
        df = pd.read_csv(file)

        print(f"\nFile: {file.name}")
        print("-" * 50)
        print(f"Rows: {len(df):,}")
        print(f"Columns: {len(df.columns)}")

        duplicates = df.duplicated().sum()
        print(f"Duplicate Rows: {duplicates:,}")

        missing_values = df.isnull().sum()
        total_missing = missing_values.sum()

        if total_missing > 0:
            print("\nMissing Values:")
            print(missing_values[missing_values > 0])
        else:
            print("\nNo Missing Values Found")