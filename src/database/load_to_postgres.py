from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

CLEANED_DIR = Path("data/cleaned")
DATABASE_URL = "postgresql+psycopg2://localhost:5433/cannabis_retail"

engine = create_engine(DATABASE_URL)


def load_csv_to_postgres(file_path):
    table_name = file_path.stem.replace("_cleaned", "")

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {file_path.name} into table: {table_name} ({len(df):,} rows)")


def main():
    csv_files = sorted(CLEANED_DIR.glob("*.csv"))

    for file_path in csv_files:
        load_csv_to_postgres(file_path)


if __name__ == "__main__":
    main()