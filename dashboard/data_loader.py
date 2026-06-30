from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "cleaned"


def load_sales():
    return pd.read_csv(DATA_DIR / "sales_transactions.csv", parse_dates=["transaction_date"])


def load_products():
    return pd.read_csv(DATA_DIR / "products.csv")


def load_data():
    sales = load_sales()
    products = load_products()
    df = sales.merge(products, on="product_id", how="left")
    return df