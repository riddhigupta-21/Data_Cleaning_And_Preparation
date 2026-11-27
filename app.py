import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="DecodeLabs | Week 4 Data Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA_PATH = Path(__file__).parent / "data.xlsx"

@st.cache_data
def load_data():
    df = pd.read_excel(DATA_PATH)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# ---------- Styling ----------
st.markdown("""
<style>
.block-container {padding-top: 1.5rem; padding-bottom: 2rem;}
[data-testid="stMetric"] {
    border: 1px solid rgba(120,120,120,.20);
    border-radius: 12px;
    padding: 12px;
}
.small-note {color:#6b7280; font-size:0.9rem;}
.insight {
    padding: 14px 16px;
    border-left: 4px solid #2563eb;
    background: rgba(37,99,235,.06);
    border-radius: 8px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.title("📊 E-Commerce Data Analytics Dashboard")
st.caption("DecodeLabs Internship • Week 4 — Data Visualization & Storytelling")
st.markdown(
    "Use the filters to explore the dataset, identify patterns, and translate them into business-focused insights."
)

# ---------- Sidebar filters ----------
st.sidebar.header("Dashboard Filters")

min_date, max_date = df["Date"].min().date(), df["Date"].max().date()
date_range = st.sidebar.date_input(
    "Date range", value=(min_date, max_date), min_value=min_date, max_value=max_date
)
if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1])
else:
    start_date, end_date = pd.Timestamp(min_date), pd.Timestamp(max_date)

products = st.sidebar.multiselect(
    "Product", sorted(df["Product"].unique()), default=sorted(df["Product"].unique())
)
statuses = st.sidebar.multiselect(
    "Order status", sorted(df["OrderStatus"].unique()), default=sorted(df["OrderStatus"].unique())
)
payments = st.sidebar.multiselect(
    "Payment method", sorted(df["PaymentMethod"].unique()), default=sorted(df["PaymentMethod"].unique())
)
referrals = st.sidebar.multiselect(
    "Referral source", sorted(df["ReferralSource"].unique()), default=sorted(df["ReferralSource"].unique())
)

filtered = df[
    (df["Date"].between(start_date, end_date))
    & (df["Product"].isin(products))
    & (df["OrderStatus"].isin(statuses))
    & (df["PaymentMethod"].isin(payments))
    & (df["ReferralSource"].isin(referrals))
].copy()

# ---------- KPIs ----------
orders = len(filtered)
revenue = filtered["TotalPrice"].sum()
avg_order = filtered["TotalPrice"].mean() if orders else 0
customers = filtered["CustomerID"].nunique()
cancel_rate = (filtered["OrderStatus"].eq("Cancelled").mean() * 100) if orders else 0

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Revenue", f"${revenue:,.2f}")
c2.metric("Orders", f"{orders:,}")
c3.metric("Avg. Order Value", f"${avg_order:,.2f}")
c4.metric("Unique Customers", f"{customers:,}")
c5.metric("Cancellation Rate", f"{cancel_rate:.1f}%")

st.divider()

if filtered.empty:
    st.warning("No records match the selected filters. Please widen the filters.")
    st.stop()

# ---------- Main narrative ----------
st.subheader("1. Revenue trend — when did sales peak?")
monthly = (
    filtered.assign(Month=filtered["Date"].dt.to_period("M").dt.to_timestamp())
    .groupby("Month", as_index=False)
    .agg(Revenue=("TotalPrice", "sum"), Orders=("OrderID", "count"))
)
fig_month = px.line(
    monthly, x="Month", y="Revenue", markers=True,
    title="Monthly Revenue",
    labels={"Revenue":"Revenue ($)", "Month":"Month"}
)
fig_month.update_layout(hovermode="x unified")
st.plotly_chart(fig_month, use_container_width=True)

peak = monthly.loc[monthly["Revenue"].idxmax()]
st.markdown(
    f'<div class="insight"><b>Action insight:</b> The highest-revenue month in the selected period was '
    f'<b>{peak["Month"].strftime("%B %Y")}</b>, generating <b>${peak["Revenue"]:,.2f}</b> across '
    f'<b>{int(peak["Orders"]):,}</b> orders.</div>',
    unsafe_allow_html=True,
)

# ---------- Product and status ----------
left, right = st.columns(2)

with left:
    st.subheader("2. Product performance")
    product_perf = (
        filtered.groupby("Product", as_index=False)
        .agg(Revenue=("TotalPrice", "sum"), Orders=("OrderID", "count"))
        .sort_values("Revenue", ascending=True)
    )
    fig_product = px.bar(
        product_perf, x="Revenue", y="Product", orientation="h",
        text_auto=".2s", title="Revenue by Product"
    )
    fig_product.update_layout(yaxis_title="", xaxis_title="Revenue ($)")
    st.plotly_chart(fig_product, use_container_width=True)

with right:
    st.subheader("3. Order status mix")
    status_perf = filtered.groupby("OrderStatus", as_index=False).agg(
        Orders=("OrderID", "count"), Revenue=("TotalPrice", "sum")
    )
    fig_status = px.bar(
        status_perf, x="OrderStatus", y="Orders",
        text_auto=True, title="Orders by Status"
    )
    fig_status.update_layout(xaxis_title="", yaxis_title="Orders")
    st.plotly_chart(fig_status, use_container_width=True)

# ---------- Customer acquisition / payments ----------
left, right = st.columns(2)

with left:
    st.subheader("4. Referral source")
    ref_perf = (
        filtered.groupby("ReferralSource", as_index=False)
        .agg(Revenue=("TotalPrice", "sum"), Orders=("OrderID", "count"))
        .sort_values("Revenue", ascending=False)
    )
    fig_ref = px.bar(
        ref_perf, x="ReferralSource", y="Revenue",
        text_auto=".2s", title="Revenue by Referral Source"
    )
    fig_ref.update_layout(xaxis_title="", yaxis_title="Revenue ($)")
    st.plotly_chart(fig_ref, use_container_width=True)

with right:
    st.subheader("5. Payment methods")
    pay_perf = (
        filtered.groupby("PaymentMethod", as_index=False)
        .agg(Revenue=("TotalPrice", "sum"), Orders=("OrderID", "count"))
        .sort_values("Revenue", ascending=False)
    )
    fig_pay = px.bar(
        pay_perf, x="PaymentMethod", y="Revenue",
        text_auto=".2s", title="Revenue by Payment Method"
    )
    fig_pay.update_layout(xaxis_title="", yaxis_title="Revenue ($)")
    st.plotly_chart(fig_pay, use_container_width=True)

# ---------- Coupon analysis ----------
st.subheader("6. Coupon performance")
coupon = filtered.copy()
coupon["CouponDisplay"] = coupon["CouponCode"].fillna("No Coupon")
coupon_perf = (
    coupon.groupby("CouponDisplay", as_index=False)
    .agg(Revenue=("TotalPrice", "sum"), Orders=("OrderID", "count"))
    .sort_values("Revenue", ascending=False)
)
fig_coupon = px.bar(
    coupon_perf, x="CouponDisplay", y="Revenue",
    text_auto=".2s", title="Revenue by Coupon Group"
)
fig_coupon.update_layout(xaxis_title="", yaxis_title="Revenue ($)")
st.plotly_chart(fig_coupon, use_container_width=True)

# ---------- Executive insights ----------
st.subheader("7. Executive takeaways")
top_product = product_perf.sort_values("Revenue", ascending=False).iloc[0]
top_ref = ref_perf.iloc[0]
top_payment = pay_perf.iloc[0]
status_counts = filtered["OrderStatus"].value_counts()
top_status = status_counts.index[0]

insights = [
    f"**Product:** {top_product['Product']} generated the highest revenue in the selected view (${top_product['Revenue']:,.2f}).",
    f"**Acquisition:** {top_ref['ReferralSource']} contributed the most revenue (${top_ref['Revenue']:,.2f}) among referral sources.",
    f"**Payments:** {top_payment['PaymentMethod']} represented the largest revenue total (${top_payment['Revenue']:,.2f}).",
    f"**Operations:** {top_status} was the most frequent order status ({int(status_counts.iloc[0]):,} orders).",
]
for item in insights:
    st.markdown(f'<div class="insight">{item}</div>', unsafe_allow_html=True)

# ---------- Data table ----------
with st.expander("View filtered data"):
    st.dataframe(filtered, use_container_width=True, hide_index=True)

st.caption("Dataset: Dataset for Data Analytics (3).xlsx • Built for DecodeLabs Internship Week 4")
