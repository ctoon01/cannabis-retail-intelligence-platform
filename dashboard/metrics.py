import streamlit as st


def display_kpis(kpis):
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "💰 Revenue",
        f"${kpis['total_revenue']:,.2f}"
    )

    col2.metric(
        "🧾 Transactions",
        f"{kpis['transactions']:,}"
    )

    col3.metric(
        "📦 Units Sold",
        f"{kpis['units_sold']:,}"
    )

    col4.metric(
        "💵 Average Sale",
        f"${kpis['average_sale']:,.2f}"
    )

    st.divider()
