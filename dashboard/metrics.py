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