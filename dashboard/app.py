import pandas as pd
import streamlit as st

from charts import (
    display_dashboard,
    monthly_revenue,
    revenue_by_category,
    revenue_by_store,
    top_brands,
)
from data_loader import load_data
from metrics import display_kpis
from styles import load_css

st.set_page_config(
    page_title="Cannabis Retail Intelligence",
    page_icon="🌿",
    layout="wide",
)

load_css()

st.title("🌿 Cannabis Retail Intelligence Dashboard")

df = load_data()

st.sidebar.header("Dashboard Filters")

selected_store = st.sidebar.selectbox(
    "Select Store",
    ["All"] + sorted(df["store_id"].dropna().astype(str).unique().tolist()),
)

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + sorted(df["category"].dropna().astype(str).unique().tolist()),
)

selected_brand = st.sidebar.selectbox(
    "Select Brand",
    ["All"] + sorted(df["brand"].dropna().astype(str).unique().tolist()),
)

min_date = df["transaction_date"].min().date()
max_date = df["transaction_date"].max().date()

selected_start, selected_end = st.sidebar.slider(
    "Date Range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
)

filtered_df = df.copy()

filtered_df = filtered_df[
    (filtered_df["transaction_date"].dt.date >= selected_start)
    & (filtered_df["transaction_date"].dt.date <= selected_end)
]

if selected_store != "All":
    filtered_df = filtered_df[filtered_df["store_id"].astype(str) == selected_store]

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["category"] == selected_category]

if selected_brand != "All":
    filtered_df = filtered_df[filtered_df["brand"] == selected_brand]

total_revenue = filtered_df["net_revenue"].sum()
estimated_profit = (
    (filtered_df["retail_price"] - filtered_df["unit_cost"])
    * filtered_df["quantity_sold"]
).sum()
profit_margin = (estimated_profit / total_revenue * 100) if total_revenue else 0

kpis = {
    "total_revenue": total_revenue,
    "estimated_profit": estimated_profit,
    "profit_margin": profit_margin,
    "transactions": len(filtered_df),
    "units_sold": filtered_df["quantity_sold"].sum(),
    "average_sale": filtered_df["net_revenue"].mean(),
}

display_kpis(kpis)

category_df = (
    filtered_df.groupby("category", as_index=False)["net_revenue"]
    .sum()
    .rename(columns={"net_revenue": "revenue"})
    .sort_values("revenue", ascending=False)
)

store_df = (
    filtered_df.groupby("store_id", as_index=False)
    .agg(revenue=("net_revenue", "sum"), transactions=("transaction_id", "count"))
    .sort_values("revenue", ascending=False)
)

brand_df = (
    filtered_df.groupby("brand", as_index=False)["net_revenue"]
    .sum()
    .rename(columns={"net_revenue": "revenue"})
    .sort_values("revenue", ascending=False)
    .head(10)
)

monthly_df = (
    filtered_df.assign(month=filtered_df["transaction_date"].dt.to_period("M").dt.to_timestamp())
    .groupby("month", as_index=False)["net_revenue"]
    .sum()
    .rename(columns={"net_revenue": "revenue"})
)

fig_category = revenue_by_category(category_df)
fig_store = revenue_by_store(store_df)
fig_brand = top_brands(brand_df)
fig_monthly = monthly_revenue(monthly_df)

display_dashboard(fig_category, fig_store, fig_brand, fig_monthly)