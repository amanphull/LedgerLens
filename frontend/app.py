import streamlit as st

from frontend.utils.api import get_uploads

st.set_page_config(
    page_title="LedgerLens",
    page_icon="📄",
)

st.title("📄 LedgerLens")

uploads = get_uploads()

st.subheader("Upload History")

st.dataframe(uploads)