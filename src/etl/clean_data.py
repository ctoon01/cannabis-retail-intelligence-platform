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
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return df


def clean_text_columns(df):
    text_cols = df.select_dtypes(include=["object", "string"]).columns

    for col in text_cols:
        df[col] = df[col].astype(str).str.strip()

    return df

def standardize_categories(df):
    if "category" not in df.columns:
        return df

    df["category"] = df["category"].astype(str).str.strip().str.lower()

    category_map = {
        "flower": "Flower",
        "flowers": "Flower",
        "vape": "Vape Cartridges",
        "vape cartridges": "Vape Cartridges",
        "edible": "Edibles",
        "edibles": "Edibles",
        "pre-rolls": "Pre-Rolls",
        "preroll": "Pre-Rolls",
        "topical": "Topicals",
        "topicals": "Topicals",
        "beverage": "Beverages",
        "beverages": "Beverages",
        "concentrate": "Concentrates",
        "concentrates": "Concentrates",
    }

    df["category"] = df["category"].replace(category_map)

    return df

def clean_dates(df):
    for col in df.columns:
        if "date" in col or "timestamp" in col:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    return df


def validate_data(df, filename):
    print(f"\nValidation Report: {filename}")
    print("-" * 50)

    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing):
        print("\nMissing Values:")
        print(missing)
    else:
        print("\nNo missing values found.")

    print("-" * 50)


def clean_file(file_path):
    df = pd.read_csv(file_path)

    original_rows = len(df)

    df = clean_column_names(df)
    df = clean_text_columns(df)
    df = standardize_categories(df)
    df = clean_dates(df)
    df = df.drop_duplicates()

    validate_data(df, file_path.name)

    output_path = CLEANED_DIR / file_path.name
    df.to_csv(output_path, index=False)

    print(
        f"Cleaned {file_path.name}: "
        f"{original_rows} rows → {len(df)} rows "
        f"({original_rows - len(df)} duplicates removed)"
    )


def main():
    csv_files = list(RAW_DIR.glob("*.csv"))

    for file_path in csv_files:
        clean_file(file_path)


if __name__ == "__main__":
    main()