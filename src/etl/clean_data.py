from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")
CLEANED_DIR = Path("data/cleaned")

CLEANED_DIR.mkdir(parents=True, exist_ok=True)


def clean_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


def clean_file(file_path):
    df = pd.read_csv(file_path)

    df = clean_column_names(df)
    df = df.drop_duplicates()

    output_path = CLEANED_DIR / file_path.name
    df.to_csv(output_path, index=False)

    print(f"Cleaned {file_path.name}: {len(df)} rows")


def main():
    csv_files = list(RAW_DIR.glob("*.csv"))

    for file_path in csv_files:
        clean_file(file_path)


if __name__ == "__main__":
    main()