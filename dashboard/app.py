import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

from charts import (
    display_dashboard,
    monthly_revenue,
    revenue_by_category,
    revenue_by_store,
    top_brands,
)
from metrics import display_kpis
from queries import (
    BRAND_QUERY,
    CATEGORY_QUERY,
    KPI_QUERY,
    MONTHLY_QUERY,
    STORE_QUERY,
    EXECUTIVE_CALLOUTS_QUERY,
)
from styles import load_css

st.set_page_config(
    page_title="Cannabis Retail Intelligence",
    page_icon="🌿",
    layout="wide",
)

load_css()

DATABASE_URL = "postgresql+psycopg2://localhost:5433/cannabis_retail"
engine = create_engine(DATABASE_URL)


@st.cache_data
def load_query(query):
    return pd.read_sql(query, engine)


st.title("🌿 Cannabis Retail Intelligence Dashboard")

st.sidebar.header("Dashboard Filters")

stores = load_query("""
SELECT DISTINCT store_id
FROM sales_transactions
ORDER BY store_id;
""")

selected_store = st.sidebar.selectbox(
    "Select Store",
    ["All"] + stores["store_id"].astype(str).tolist(),
)

categories = load_query("""
SELECT DISTINCT category
FROM products
ORDER BY category;
""")

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + categories["category"].astype(str).tolist(),
)

brands = load_query("""
SELECT DISTINCT brand
FROM products
ORDER BY brand;
""")

selected_brand = st.sidebar.selectbox(
    "Select Brand",
    ["All"] + brands["brand"].astype(str).tolist(),
)

date_bounds = load_query("""
SELECT
    MIN(transaction_date::date) AS min_date,
    MAX(transaction_date::date) AS max_date
FROM sales_transactions
WHERE transaction_date IS NOT NULL;
""")

min_date = pd.to_datetime(date_bounds["min_date"].iloc[0]).date()
max_date = pd.to_datetime(date_bounds["max_date"].iloc[0]).date()

selected_start, selected_end = st.sidebar.slider(
    "Date Range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
)

filters = [
    f"s.transaction_date::date BETWEEN '{selected_start}' AND '{selected_end}'"
]

if selected_store != "All":
    filters.append(f"s.store_id = {selected_store}")

if selected_category != "All":
    filters.append(f"p.category = '{selected_category}'")

if selected_brand != "All":
    filters.append(f"p.brand = '{selected_brand}'")

where_clause = "WHERE " + " AND ".join(filters)

kpi_df = load_query(KPI_QUERY.format(where_clause=where_clause))
category_df = load_query(CATEGORY_QUERY.format(where_clause=where_clause))
brand_df = load_query(BRAND_QUERY.format(where_clause=where_clause))
store_df = load_query(STORE_QUERY.format(where_clause=where_clause))
monthly_df = load_query(MONTHLY_QUERY.format(where_clause=where_clause))

callouts_df = load_query(EXECUTIVE_CALLOUTS_QUERY.format(where_clause=where_clause))
callouts = callouts_df.iloc[0]

callout1, callout2, callout3 = st.columns(3)

callout1.metric("🏪 Top Store", callouts["top_store"])
callout2.metric("🏷️ Top Brand", callouts["top_brand"])
callout3.metric("🌿 Top Category", callouts["top_category"])

st.divider()

display_kpis(kpi_df.iloc[0])

fig_category = revenue_by_category(category_df)
fig_store = revenue_by_store(store_df)
fig_brand = top_brands(brand_df)
fig_monthly = monthly_revenue(monthly_df)

display_dashboard(fig_category, fig_store, fig_brand, fig_monthly)