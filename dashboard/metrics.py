import streamlit as st


def display_kpis(kpis):
    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Revenue", f"${kpis['total_revenue']:,.2f}")
    col2.metric("💵 Estimated Profit", f"${kpis['estimated_profit']:,.2f}")
    col3.metric("📈 Profit Margin", f"{kpis['profit_margin']:,.2f}%")

    col4, col5, col6 = st.columns(3)

    col4.metric("🧾 Transactions", f"{kpis['transactions']:,}")
    col5.metric("📦 Units Sold", f"{kpis['units_sold']:,}")
    col6.metric("💳 Average Sale", f"${kpis['average_sale']:,.2f}")

    st.divider()


def display_callouts(callouts):
    col1, col2, col3 = st.columns(3)

    col1.metric("🏪 Top Store", callouts["top_store"])
    col2.metric("🏷️ Top Brand", callouts["top_brand"])
    col3.metric("🌿 Top Category", callouts["top_category"])

    st.divider()