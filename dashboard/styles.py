import streamlit as st


def load_css():
    st.markdown("""
    <style>

    .block-container{
        padding-top:2rem;
        padding-bottom:2rem;
    }

    h1{
        color:#2E8B57;
    }

    div[data-testid="metric-container"]{
        background-color:#f7f7f7;
        border-radius:12px;
        padding:15px;
        border:1px solid #ddd;
    }

    </style>
    """, unsafe_allow_html=True)