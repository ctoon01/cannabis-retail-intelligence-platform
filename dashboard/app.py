import pandas as pd
import plotly.express as px
import streamlit as st
from sqlalchemy import create_engine

# Page setup
st.set_page_config(
    page_title="Cannabis Retail Intelligence",
    page_icon="🌿",
    layout="wide",
)

# Database connection
DATABASE_URL = "postgresql+psycopg2://localhost:5433/cannabis_retail"
engine = create_engine(DATABASE_URL)


@st.cache_data
def load_query(query):
    return pd.read_sql(query, engine)


# Title
st.title("🌿 Cannabis Retail Intelligence Dashboard")

# Sidebar filters
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

store_filter = "" if selected_store == "All" else f"WHERE store_id = {selected_store}"
store_filter_with_alias = "" if selected_store == "All" else f"WHERE s.store_id = {selected_store}"

# KPI query
kpi_query = f"""
SELECT
    ROUND(SUM(net_revenue)::numeric, 2) AS total_revenue,
    ROUND(AVG(net_revenue)::numeric, 2) AS average_sale,
    COUNT(*) AS transactions,
    SUM(quantity_sold) AS units_sold
FROM sales_transactions
{store_filter};
"""

kpis = load_query(kpi_query).iloc[0]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${kpis['total_revenue']:,.2f}")
col2.metric("Transactions", f"{kpis['transactions']:,}")
col3.metric("Units Sold", f"{kpis['units_sold']:,}")
col4.metric("Average Sale", f"${kpis['average_sale']:,.2f}")

st.divider()

# Revenue by category
category_query = f"""
SELECT
    p.category,
    ROUND(SUM(s.net_revenue)::numeric, 2) AS revenue
FROM sales_transactions s
JOIN products p
    ON s.product_id = p.product_id
{store_filter_with_alias}
GROUP BY p.category
ORDER BY revenue DESC;
"""

category_df = load_query(category_query)

fig_category = px.bar(
    category_df,
    x="category",
    y="revenue",
    title="Revenue by Category",
)

# Top brands
brand_query = f"""
SELECT
    p.brand,
    ROUND(SUM(s.net_revenue)::numeric, 2) AS revenue
FROM sales_transactions s
JOIN products p
    ON s.product_id = p.product_id
{store_filter_with_alias}
GROUP BY p.brand
ORDER BY revenue DESC
LIMIT 10;
"""

brand_df = load_query(brand_query)

fig_brand = px.bar(
    brand_df,
    x="revenue",
    y="brand",
    orientation="h",
    title="Top 10 Brands by Revenue",
)

# Revenue by store
store_query = """
SELECT
    store_id,
    ROUND(SUM(net_revenue)::numeric, 2) AS revenue,
    COUNT(*) AS transactions
FROM sales_transactions
GROUP BY store_id
ORDER BY revenue DESC;
"""

store_df = load_query(store_query)

fig_store = px.bar(
    store_df,
    x="store_id",
    y="revenue",
    title="Revenue by Store",
)

# Monthly revenue trend
monthly_query = f"""
SELECT
    DATE_TRUNC('month', transaction_date::date) AS month,
    ROUND(SUM(net_revenue)::numeric, 2) AS revenue
FROM sales_transactions
WHERE transaction_date IS NOT NULL
{"AND store_id = " + selected_store if selected_store != "All" else ""}
GROUP BY month
ORDER BY month;
"""

monthly_df = load_query(monthly_query)

fig_monthly = px.line(
    monthly_df,
    x="month",
    y="revenue",
    title="Monthly Revenue Trend",
    markers=True,
)

# Dashboard layout
left, right = st.columns(2)

with left:
    st.plotly_chart(fig_category, use_container_width=True)

with right:
    st.plotly_chart(fig_store, use_container_width=True)

left, right = st.columns(2)

with left:
    st.plotly_chart(fig_brand, use_container_width=True)

with right:
    st.plotly_chart(fig_monthly, use_container_width=True)