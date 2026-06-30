from styles import load_css
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
)

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

stores = load_query(
    """
    SELECT DISTINCT store_id
    FROM sales_transactions
    ORDER BY store_id;
    """
)

selected_store = st.sidebar.selectbox(
    "Select Store",
    ["All"] + stores["store_id"].astype(str).tolist(),
)

categories = load_query(
    """
    SELECT DISTINCT category
    FROM products
    ORDER BY category;
    """
)

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + categories["category"].astype(str).tolist(),
)

brands = load_query(
    """
    SELECT DISTINCT brand
    FROM products
    ORDER BY brand;
    """
)

selected_brand = st.sidebar.selectbox(
    "Select Brand",
    ["All"] + brands["brand"].astype(str).tolist(),
)


filters = []
filters_with_alias = []

if selected_store != "All":
    filters.append(f"store_id = {selected_store}")
    filters_with_alias.append(f"s.store_id = {selected_store}")

if selected_category != "All":
    filters_with_alias.append(f"p.category = '{selected_category}'")

if selected_brand != "All":
    filters_with_alias.append(f"p.brand = '{selected_brand}'")

store_filter = "WHERE " + " AND ".join(filters) if filters else ""
store_filter_with_alias = "WHERE " + " AND ".join(filters_with_alias) if filters_with_alias else ""

monthly_store_filter = (
    "AND " + " AND ".join(filters)
    if filters
    else ""
)

kpi_df = load_query(KPI_QUERY.format(store_filter_with_alias=store_filter_with_alias))
category_df = load_query(CATEGORY_QUERY.format(store_filter_with_alias=store_filter_with_alias))
brand_df = load_query(BRAND_QUERY.format(store_filter_with_alias=store_filter_with_alias))
store_df = load_query(STORE_QUERY)
monthly_df = load_query(MONTHLY_QUERY.format(monthly_store_filter=monthly_store_filter))

display_kpis(kpi_df.iloc[0])

fig_category = revenue_by_category(category_df)
fig_store = revenue_by_store(store_df)
fig_brand = top_brands(brand_df)
fig_monthly = monthly_revenue(monthly_df)

display_dashboard(fig_category, fig_store, fig_brand, fig_monthly)