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

from datetime import datetime

st.title("📄 LedgerLens")

header_col1, header_col2 = st.columns([3, 1])

with header_col1:
    st.caption("AI Powered Invoice Processing System")

with header_col2:
    st.markdown(
        f"**📅 {datetime.now().strftime('%d %b %Y')}**"
    )

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
        processed = approved + rejected

        if total_invoices > 0:
            progress = processed / total_invoices
        else:
            progress = 0

        st.subheader("📈 Overall Review Progress")
        st.progress(progress)

        st.caption(
            f"{processed} of {total_invoices} invoices reviewed"
        )
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
# ==========================================
# Analytics Charts
# ==========================================

st.divider()

chart_col1, chart_col2 = st.columns(2)

with chart_col1:

    if not df.empty and "review_status" in df.columns:

        review_chart = (
            df["review_status"]
            .value_counts()
            .reset_index()
        )

        review_chart.columns = [
            "Status",
            "Count",
        ]

        fig = px.pie(
            review_chart,
            names="Status",
            values="Count",
            title="Review Status",
            hole=0.45,
            color="Status",
            color_discrete_map={
                "Approved": "#2ECC71",
                "Rejected": "#E74C3C",
                "Pending": "#F39C12",
            },
        )
        fig.update_traces(
            textposition="inside",
            textinfo="percent+label",
        )

        fig.update_layout(
            showlegend=True,
            legend_title="Status",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )
# ==========================================
# Top Vendors & Recent Activity
# ==========================================

st.divider()

vendor_col, activity_col = st.columns(2)

with vendor_col:

    st.subheader("🏢 Top Vendors")

    if (
        not df.empty
        and "vendor_name" in df.columns
    ):

        vendor_df = df.copy()

        vendor_df["vendor_name"] = (
            vendor_df["vendor_name"]
            .fillna("Unknown Vendor")
            .replace("", "Unknown Vendor")
        )

        top_vendors = (
            vendor_df["vendor_name"]
            .value_counts()
            .head(5)
            .reset_index()
        )

        top_vendors.columns = [
            "Vendor",
            "Invoices",
        ]

        st.dataframe(
            top_vendors,
            use_container_width=True,
            hide_index=True,
        )

    else:
        st.info("No vendor data available.")
with activity_col:

    st.subheader("🕒 Recent Activity")

    if (
        not df.empty
        and "upload_time" in df.columns
    ):

        activity_df = df.copy()

        activity_df["upload_time"] = pd.to_datetime(
            activity_df["upload_time"],
            errors="coerce",
        )

        activity_df = activity_df.sort_values(
            "upload_time",
            ascending=False,
        )

        latest = activity_df.head(5)

        for _, row in latest.iterrows():

            filename = row.get(
                "original_filename",
                "Invoice",
            )

            status = row.get(
                "review_status",
                "Pending",
            )

            upload_time = row.get(
                "upload_time",
            )

            if pd.notna(upload_time):
                time_text = upload_time.strftime(
                    "%d-%m-%Y %H:%M"
                )
            else:
                time_text = "-"

            st.write(
                f"**{filename}**"
            )
            st.caption(
                f"{status} • {time_text}"
            )

    else:
        st.info("No recent activity.")
with chart_col2:

    if not df.empty and "ai_status" in df.columns:

        ai_chart = (
            df["ai_status"]
            .value_counts()
            .reset_index()
        )

        ai_chart.columns = [
            "Status",
            "Count",
        ]

        fig = px.bar(
            ai_chart,
            x="Status",
            y="Count",
            title="AI Processing Status",
            color="Status",
            text="Count",
            color_discrete_map={
                "Completed": "#2ECC71",
                "Pending": "#F39C12",
                "Failed": "#E74C3C",
            },
        )
        fig.update_traces(
            textposition="outside",
        )

        fig.update_layout(
            showlegend=False,
            xaxis_title="",
            yaxis_title="Invoices",
        )
        st.plotly_chart(
            fig,
            use_container_width=True,
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

# ==========================================
# Advanced Search & Filters
# ==========================================


st.subheader("🔍 Search & Filters")

c1, c2, c3 = st.columns(3)

with c1:

    search = st.text_input(
        "Filename",
        placeholder="Search filename...",
    )

with c2:

    vendor_filter = st.text_input(
        "Vendor",
        placeholder="Search vendor...",
    )

with c3:

    invoice_filter = st.text_input(
        "Invoice Number",
        placeholder="Search invoice number...",
    )

c4, c5 = st.columns(2)

with c4:

    ai_filter = st.selectbox(
        "AI Status",
        [
            "All",
            "Pending",
            "Completed",
            "Failed",
        ],
    )

with c5:

    review_filter = st.selectbox(
        "Review Status",
        [
            "All",
            "Pending",
            "Approved",
            "Rejected",
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
        vendor_filter
        and "vendor_name" in df.columns
    ):

        df = df[
            df["vendor_name"]
            .fillna("")
            .str.contains(
                vendor_filter,
                case=False,
                na=False,
            )
        ]

    if (
        invoice_filter
        and "invoice_number" in df.columns
    ):

        df = df[
            df["invoice_number"]
            .fillna("")
            .str.contains(
                invoice_filter,
                case=False,
                na=False,
            )
        ]

    if (
        ai_filter != "All"
        and "ai_status" in df.columns
    ):

        df = df[
            df["ai_status"] == ai_filter
        ]

    if (
        review_filter != "All"
        and "review_status" in df.columns
    ):

        df = df[
            df["review_status"] == review_filter
        ]
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

                st.markdown(f"""
                **🏢 Vendor**  
                {row.get("vendor_name", "-")}

                **📄 Invoice No.**  
                {row.get("invoice_number", "-")}

                **📅 Invoice Date**  
                {row.get("invoice_date", "-")}

                **🆔 GST Number**  
                {row.get("gst_number", "-")}
                    """)

            with info2:

                st.markdown(f"""
                **💰 Total Amount**  
                ₹ {row.get("total_amount", "-")}

                **💵 Tax Amount**  
                ₹ {row.get("tax_amount", "-")}
                """)

                            # -----------------------------
                # AI Status Badge
                # -----------------------------

                ai_status = row.get("ai_status", "Pending")

                if ai_status == "Completed":
                    st.success(f"🤖 AI Status : {ai_status}")

                elif ai_status == "Failed":
                    st.error(f"🤖 AI Status : {ai_status}")

                else:
                    st.warning(f"🤖 AI Status : {ai_status}")

                # -----------------------------
                # Review Status Badge
                # -----------------------------

                review_status = row.get("review_status", "Pending")

                if review_status == "Approved":
                    st.success(f"✅ Review : {review_status}")

                elif review_status == "Rejected":
                    st.error(f"❌ Review : {review_status}")

                else:
                    st.warning(f"📝 Review : {review_status}")

            st.write("")

            b1, b2, b3 = st.columns(3)

            upload_id = row["id"]

            ai_status = row.get("ai_status", "Pending")
            review_status = row.get("review_status", "Pending")

            with b1:
                if ai_status == "Pending":
                    if st.button("🤖 Process AI", key=f"process_{upload_id}", use_container_width=True):
                        with st.spinner("Processing invoice..."):
                            try:
                                process_invoice(upload_id)
                                st.success("AI Processing Completed")
                                st.rerun()
                            except Exception as e:
                                st.error(e)
                else:
                    st.success("✅ AI Completed")

            with b2:
                if review_status == "Pending":
                    if st.button("✅ Approve", key=f"approve_{upload_id}", use_container_width=True):
                        try:
                            approve_invoice(upload_id)
                            st.success("Invoice Approved")
                            st.rerun()
                        except Exception as e:
                            st.error(e)
                elif review_status == "Approved":
                    st.success("✔ Approved")
                else:
                    st.empty()

            with b3:
                if review_status == "Pending":
                    if st.button("❌ Reject", key=f"reject_{upload_id}", use_container_width=True):
                        try:
                            reject_invoice(upload_id)
                            st.warning("Invoice Rejected")
                            st.rerun()
                        except Exception as e:
                            st.error(e)
                elif review_status == "Rejected":
                    st.error("✖ Rejected")
                else:
                    st.empty()


            st.divider()
# ==========================================
# Dashboard Summary
# ==========================================


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
    f"LedgerLens • AI Powered Invoice Processing System • "
    f"Last Refreshed: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)