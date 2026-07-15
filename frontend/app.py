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
st.caption("AI Powered Invoice Processing System")

left, right = st.columns([1, 1])

with left:

    st.subheader("Upload Invoice")

    uploaded_file = render_uploader()

    if uploaded_file:

        if st.button("Upload Invoice", use_container_width=True):

            with st.spinner("Uploading invoice..."):

                result = upload_file(uploaded_file)

            st.success("Invoice Uploaded Successfully!")

            st.json(result)

with right:

    st.subheader("Preview")

    if uploaded_file:

        st.image(
            uploaded_file,
            use_container_width=True,
        )

    else:

        st.info("Select an invoice to preview.")

st.divider()

history = get_uploads()

st.subheader("📊 Upload Statistics")

st.metric(
    label="Total Uploaded Documents",
    value=len(history),
)

st.divider()

st.subheader("📋 Upload History")

st.dataframe(
    history,
    use_container_width=True,
)