import streamlit as st


def display_insights(kpis, callouts, category_df, store_df):
    top_category_share = 0
    top_store_share = 0

    if kpis["total_revenue"] > 0:
        top_category_share = category_df["revenue"].iloc[0] / kpis["total_revenue"] * 100
        top_store_share = store_df["revenue"].iloc[0] / kpis["total_revenue"] * 100

    st.subheader("📌 Executive Insights")

    st.markdown(
        f"""
        - **{callouts["top_category"]}** is the leading category, representing approximately **{top_category_share:.1f}%** of filtered revenue.
        - **Store {callouts["top_store"]}** is the top-performing store, contributing approximately **{top_store_share:.1f}%** of filtered revenue.
        - **{callouts["top_brand"]}** is the highest-revenue brand for the selected filters.
        - The current filtered dataset includes **{kpis["transactions"]:,} transactions** and **{kpis["units_sold"]:,} units sold**.
        """
    )

    st.divider()