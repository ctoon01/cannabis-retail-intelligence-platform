import plotly.express as px
import streamlit as st


def revenue_by_category(df):
    fig = px.pie(
        df,
        names="category",
        values="revenue",
        title="Revenue Share by Category",
        hole=0.45,
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    return fig


def revenue_by_store(df):
    return px.bar(df, x="store_id", y="revenue", title="Revenue by Store")


def top_brands(df):
    return px.bar(
        df,
        x="revenue",
        y="brand",
        orientation="h",
        title="Top 10 Brands by Revenue",
    )


def monthly_revenue(df):
    return px.line(
        df,
        x="month",
        y="revenue",
        markers=True,
        title="Monthly Revenue Trend",
    )


def display_dashboard(fig1, fig2, fig3, fig4):
    left, right = st.columns(2)

    with left:
        st.plotly_chart(fig1, use_container_width=True)

    with right:
        st.plotly_chart(fig2, use_container_width=True)

    left, right = st.columns(2)

    with left:
        st.plotly_chart(fig3, use_container_width=True)

    with right:
        st.plotly_chart(fig4, use_container_width=True)