import pandas as pd
import streamlit as st
import plotly.express as px

from frontend.components.uploader import render_uploader
from frontend.utils.api import (
    approve_invoice,
    get_uploads,
    process_invoice,
    reject_invoice,
    upload_file,
)
# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="LedgerLens",
    page_icon="📄",
    layout="wide",
)

st.title("📄 LedgerLens")
st.caption("AI Powered Invoice Processing System")

# -----------------------------------
# Load Data
# -----------------------------------

history = get_uploads()

df = pd.DataFrame(history)
# ==========================================
# Financial Analytics
# ==========================================

total_invoice_amount = 0
total_tax_amount = 0
average_invoice = 0
max_invoice = 0
min_invoice = 0

if not df.empty:

    if "total_amount" in df.columns:
        df["total_amount"] = (
            pd.to_numeric(
                df["total_amount"],
                errors="coerce",
            )
            .fillna(0)
        )

        total_invoice_amount = df["total_amount"].sum()
        average_invoice = df["total_amount"].mean()
        max_invoice = df["total_amount"].max()
        min_invoice = df["total_amount"].min()

    if "tax_amount" in df.columns:
        df["tax_amount"] = (
            pd.to_numeric(
                df["tax_amount"],
                errors="coerce",
            )
            .fillna(0)
        )

        total_tax_amount = df["tax_amount"].sum()
# -----------------------------------
# Dashboard Metrics
# -----------------------------------

total_invoices = len(df)

ai_completed = 0
pending_review = 0
approved = 0
rejected = 0

if not df.empty:

    if "ai_status" in df.columns:
        ai_completed = (
            df["ai_status"] == "Completed"
        ).sum()

    if "review_status" in df.columns:
        pending_review = (
            df["review_status"] == "Pending"
        ).sum()

        approved = (
            df["review_status"] == "Approved"
        ).sum()

        rejected = (
            df["review_status"] == "Rejected"
        ).sum()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "📄 Total",
        total_invoices,
    )

with col2:
    st.metric(
        "🤖 AI Completed",
        ai_completed,
    )

with col3:
    st.metric(
        "📝 Pending",
        pending_review,
    )

with col4:
    st.metric(
        "✅ Approved",
        approved,
    )

with col5:
    st.metric(
        "❌ Rejected",
        rejected,
    )

st.divider()

f1, f2, f3 = st.columns(3)

with f1:
    st.metric(
        "💰 Total Invoice Amount",
        f"₹ {total_invoice_amount:,.2f}",
    )

with f2:
    st.metric(
        "💵 Total Tax",
        f"₹ {total_tax_amount:,.2f}",
    )

with f3:
    st.metric(
        "📈 Average Invoice",
        f"₹ {average_invoice:,.2f}",
    )

# -----------------------------------
# Upload Section
# -----------------------------------

left, right = st.columns([1, 1])

with left:

    st.subheader("Upload Invoice")

    uploaded_file = render_uploader()

    if uploaded_file:

        if st.button(
            "📤 Upload Invoice",
            use_container_width=True,
        ):

            with st.spinner("Uploading Invoice..."):

                try:

                    result = upload_file(
                        uploaded_file
                    )

                    st.success(
                        "Invoice Uploaded Successfully"
                    )

                    st.json(result)

                    st.rerun()

                except Exception as e:

                    st.error(str(e))

with right:

    st.subheader("Preview")

    if uploaded_file:

        st.image(
            uploaded_file,
            use_container_width=True,
        )

    else:

        st.info(
            "No Preview Available"
        )

st.divider()

# -----------------------------------
# Search & Filters
# -----------------------------------

search_col, filter_col = st.columns([3, 1])

with search_col:

    search = st.text_input(
        "🔍 Search Invoice",
        placeholder="Search by filename...",
    )

with filter_col:

    status_filter = st.selectbox(
        "AI Status",
        [
            "All",
            "Completed",
            "Pending",
            "Failed",
        ],
    )

if not df.empty:

    if search:

        df = df[
            df["original_filename"]
            .str.contains(
                search,
                case=False,
                na=False,
            )
        ]

    if (
        status_filter != "All"
        and "ai_status" in df.columns
    ):

        df = df[
            df["ai_status"]
            == status_filter
        ]

st.divider()

st.subheader("Invoice History")
if df.empty:

    st.info("No invoices uploaded yet.")

else:

    for _, row in df.iterrows():

        filename = row.get(
            "original_filename",
            "Unknown File",
        )

        with st.container(border=True):

            st.markdown(f"### 📄 {filename}")

            info1, info2 = st.columns(2)

            with info1:

                st.write(
                    "**Vendor:**",
                    row.get("vendor_name", "-"),
                )

                st.write(
                    "**Invoice Number:**",
                    row.get("invoice_number", "-"),
                )

                st.write(
                    "**Invoice Date:**",
                    row.get("invoice_date", "-"),
                )

                st.write(
                    "**GST Number:**",
                    row.get("gst_number", "-"),
                )

            with info2:

                st.write(
                    "**Total Amount:**",
                    row.get("total_amount", "-"),
                )

                st.write(
                    "**Tax Amount:**",
                    row.get("tax_amount", "-"),
                )

                st.write(
                    "**AI Status:**",
                    row.get("ai_status", "Pending"),
                )

                st.write(
                    "**Review Status:**",
                    row.get("review_status", "Pending"),
                )

            st.write("")

            b1, b2, b3 = st.columns(3)

            upload_id = row["id"]

            with b1:

                if st.button(
                    "🤖 Process AI",
                    key=f"process_{upload_id}",
                    use_container_width=True,
                ):

                    with st.spinner(
                        "Processing invoice..."
                    ):

                        try:

                            process_invoice(
                                upload_id
                            )

                            st.success(
                                "AI Processing Completed"
                            )

                            st.rerun()

                        except Exception as e:

                            st.error(e)

            with b2:

                if st.button(
                    "✅ Approve",
                    key=f"approve_{upload_id}",
                    use_container_width=True,
                ):

                    try:

                        approve_invoice(
                            upload_id
                        )

                        st.success(
                            "Invoice Approved"
                        )

                        st.rerun()

                    except Exception as e:

                        st.error(e)

            with b3:

                if st.button(
                    "❌ Reject",
                    key=f"reject_{upload_id}",
                    use_container_width=True,
                ):

                    try:

                        reject_invoice(
                            upload_id
                        )

                        st.warning(
                            "Invoice Rejected"
                        )

                        st.rerun()

                    except Exception as e:

                        st.error(e)

            st.divider()
            # ==========================================
# Dashboard Summary
# ==========================================

st.divider()

st.subheader("📊 Dashboard Summary")

summary_col1, summary_col2 = st.columns(2)

with summary_col1:

    if not df.empty and "ai_status" in df.columns:

        ai_summary = (
            df["ai_status"]
            .value_counts()
            .reset_index()
        )

        ai_summary.columns = [
            "AI Status",
            "Count",
        ]

        st.write("### AI Processing Summary")
        st.dataframe(
            ai_summary,
            use_container_width=True,
            hide_index=True,
        )

with summary_col2:

    if (
        not df.empty
        and "review_status" in df.columns
    ):

        review_summary = (
            df["review_status"]
            .value_counts()
            .reset_index()
        )

        review_summary.columns = [
            "Review Status",
            "Count",
        ]

        st.write("### Review Summary")
        st.dataframe(
            review_summary,
            use_container_width=True,
            hide_index=True,
        )

# ==========================================
# Download CSV
# ==========================================

st.divider()

if not df.empty:

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="📥 Download Invoice Data (CSV)",
        data=csv,
        file_name="ledgerlens_invoices.csv",
        mime="text/csv",
        use_container_width=True,
    )

# ==========================================
# Refresh
# ==========================================

refresh_col1, refresh_col2 = st.columns([1, 5])

with refresh_col1:

    if st.button(
        "🔄 Refresh",
        use_container_width=True,
    ):
        st.rerun()

# ==========================================
# Footer
# ==========================================

st.divider()

st.caption(
    "LedgerLens • AI Powered Invoice Processing System"
)