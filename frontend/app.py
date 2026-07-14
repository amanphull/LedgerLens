import streamlit as st

from frontend.components.uploader import render_uploader
from frontend.utils.api import (
    get_uploads,
    upload_file,
)

st.set_page_config(
    page_title="LedgerLens",
    page_icon="📄",
    layout="wide",
)

st.title("📄 LedgerLens")

st.subheader("Upload Invoice")

uploaded_file = render_uploader()

if uploaded_file:

    st.image(uploaded_file, width=300)

    if st.button("Upload Invoice"):

        with st.spinner("Uploading..."):

            result = upload_file(uploaded_file)

        st.success("Upload Successful!")

        st.json(result)

st.divider()

st.subheader("Upload History")

history = get_uploads()

st.dataframe(
    history,
    use_container_width=True,
)