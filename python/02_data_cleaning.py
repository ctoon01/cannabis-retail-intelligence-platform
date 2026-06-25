import pandas as pd
from pathlib import Path

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_PATH = PROJECT_ROOT / "data" / "raw"
CLEANED_PATH = PROJECT_ROOT / "data" / "cleaned"

CLEANED_PATH.mkdir(parents=True, exist_ok=True)

CLEANED_PATH.mkdir(exist_ok=True)

print("=" * 50)
print("DATA CLEANING")
print("=" * 50)

# ------------------------
# SALES TRANSACTIONS
# ------------------------

sales = pd.read_csv(RAW_PATH / "sales_transactions.csv")

print(f"\nOriginal Sales Rows: {len(sales):,}")

# Remove duplicates
sales = sales.drop_duplicates()

print(f"After Removing Duplicates: {len(sales):,}")

# Replace missing discounts with 0
sales["discount_amount"] = sales["discount_amount"].fillna(0)

# Save cleaned file
sales.to_csv(CLEANED_PATH / "sales_transactions_cleaned.csv", index=False)

print("✔ sales_transactions cleaned")


# ------------------------
# PRODUCTS
# ------------------------

products = pd.read_csv(RAW_PATH / "products.csv")

print(f"\nOriginal Products Rows: {len(products):,}")

products = products.drop_duplicates()

products["brand"] = products["brand"].fillna("Unknown")
products["cbd_percent"] = products["cbd_percent"].fillna(0)

products.to_csv(CLEANED_PATH / "products_cleaned.csv", index=False)

print("✔ products cleaned")