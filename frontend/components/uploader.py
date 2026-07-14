import streamlit as st


def render_uploader():
    return st.file_uploader(
        "Choose an invoice",
        type=["jpg", "jpeg", "png"],
    )