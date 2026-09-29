import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Retail Business Analytics", page_icon="📊", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data/retail_sales.csv")
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
    df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")
    df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
    df["Profit_Margin"] = (df["Profit"] / df["Revenue"].replace(0, pd.NA) * 100).astype(float)
    return df

df = load_data()

st.title("📊 Retail Business Analytics")
st.markdown("**Data Analyst Trainee Portfolio Project** · Data Quality → EDA → SQL Analysis → KPI Dashboard → Business Insights")

with st.sidebar:
    st.header("🎛️ Analysis Filters")
    date_range = st.date_input(
        "Order date range",
        value=(df["Order_Date"].min().date(), df["Order_Date"].max().date())
    )
    regions = st.multiselect("Region", sorted(df["Region"].unique()), default=sorted(df["Region"].unique()))
    categories = st.multiselect("Category", sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))
    segments = st.multiselect("Customer Segment", sorted(df["Customer_Segment"].unique()), default=sorted(df["Customer_Segment"].unique()))

if len(date_range) == 2:
    start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
else:
    start, end = df["Order_Date"].min(), df["Order_Date"].max()

f = df[
    (df["Order_Date"].between(start, end)) &
    (df["Region"].isin(regions)) &
    (df["Category"].isin(categories)) &
    (df["Customer_Segment"].isin(segments))
].copy()

revenue=f["Revenue"].sum()
profit=f["Profit"].sum()
orders=f["Order_ID"].nunique()
units=f["Quantity"].sum()
aov=revenue/orders if orders else 0
margin=(profit/revenue*100) if revenue else 0

c1,c2,c3,c4,c5=st.columns(5)
c1.metric("Revenue", f"${revenue:,.0f}")
c2.metric("Profit", f"${profit:,.0f}")
c3.metric("Orders", f"{orders:,}")
c4.metric("Units Sold", f"{units:,}")
c5.metric("Avg Order Value", f"${aov:,.0f}")

st.caption(f"Filtered records: {len(f):,} | Profit margin: {margin:.1f}%")

tab1,tab2,tab3,tab4=st.tabs(["📈 Executive Dashboard","🔎 Product & Customer","🧹 Data Quality","💡 Business Insights"])

with tab1:
    a,b=st.columns(2)
    with a:
        monthly=f.assign(Month=f["Order_Date"].dt.to_period("M").astype(str)).groupby("Month",as_index=False).agg(Revenue=("Revenue","sum"),Profit=("Profit","sum"))
        fig=px.line(monthly,x="Month",y=["Revenue","Profit"],markers=True,title="Monthly Revenue & Profit")
        st.plotly_chart(fig,use_container_width=True)
    with b:
        reg=f.groupby("Region",as_index=False).agg(Revenue=("Revenue","sum"),Profit=("Profit","sum"))
        fig=px.bar(reg,x="Region",y="Revenue",color="Region",text_auto=".2s",title="Regional Revenue")
        st.plotly_chart(fig,use_container_width=True)

    cat=f.groupby("Category",as_index=False).agg(Revenue=("Revenue","sum"),Profit=("Profit","sum"))
    fig=px.bar(cat,x="Category",y=["Revenue","Profit"],barmode="group",title="Category Revenue vs Profit")
    st.plotly_chart(fig,use_container_width=True)

with tab2:
    left,right=st.columns(2)
    with left:
        top=f.groupby("Product",as_index=False).agg(Revenue=("Revenue","sum"),Profit=("Profit","sum"),Units=("Quantity","sum")).sort_values("Revenue",ascending=False).head(10)
        fig=px.bar(top.sort_values("Revenue"),x="Revenue",y="Product",orientation="h",title="Top 10 Products by Revenue")
        st.plotly_chart(fig,use_container_width=True)
    with right:
        seg=f.groupby("Customer_Segment",as_index=False).agg(Revenue=("Revenue","sum"),Profit=("Profit","sum"),Orders=("Order_ID","nunique"))
        fig=px.pie(seg,names="Customer_Segment",values="Revenue",hole=.45,title="Revenue by Customer Segment")
        st.plotly_chart(fig,use_container_width=True)

    st.subheader("Product Profitability")
    prod=f.groupby("Product",as_index=False).agg(Revenue=("Revenue","sum"),Profit=("Profit","sum"))
    prod["Margin %"]=(prod["Profit"]/prod["Revenue"]*100).round(2)
    st.dataframe(prod.sort_values("Margin %",ascending=False),use_container_width=True)

with tab3:
    st.subheader("Data Quality Checks")
    q1,q2,q3,q4=st.columns(4)
    q1.metric("Rows",f"{len(df):,}")
    q2.metric("Columns",f"{len(df.columns):,}")
    q3.metric("Missing Cells",f"{int(df.isna().sum().sum()):,}")
    q4.metric("Duplicate Rows",f"{int(df.duplicated().sum()):,}")
    quality=pd.DataFrame({
        "Check":["Missing values","Duplicate rows","Duplicate Order IDs","Invalid dates","Negative revenue"],
        "Result":[
            int(df.isna().sum().sum()),
            int(df.duplicated().sum()),
            int(df["Order_ID"].duplicated().sum()),
            int(df["Order_Date"].isna().sum()),
            int((df["Revenue"]<0).sum())
        ]
    })
    st.dataframe(quality,use_container_width=True)
    st.info("The dataset is validated before KPI and visualization calculations.")

with tab4:
    st.subheader("Actionable Business Insights")
    if len(f):
        best_region=f.groupby("Region")["Revenue"].sum().idxmax()
        best_category=f.groupby("Category")["Profit"].sum().idxmax()
        best_product=f.groupby("Product")["Revenue"].sum().idxmax()
        worst_margin=f.groupby("Product")["Profit_Margin"].mean().idxmin()
        st.success(f"**1. Regional performance:** {best_region} contributes the highest revenue in the selected period.")
        st.success(f"**2. Profit driver:** {best_category} generates the highest total profit.")
        st.success(f"**3. Product opportunity:** {best_product} is the top product by revenue.")
        st.warning(f"**4. Investigation area:** {worst_margin} has the lowest average product margin and should be reviewed for pricing/cost efficiency.")
        st.markdown("### Recommended analyst actions")
        st.markdown("- Monitor low-margin products and review pricing/discount patterns.\n- Compare regional performance monthly to detect underperforming markets.\n- Prioritize high-revenue/high-margin products for inventory and marketing decisions.\n- Track KPIs regularly through the dashboard instead of manual reporting.")

st.divider()
st.subheader("📋 Filtered Transaction Data")
st.dataframe(f.sort_values("Order_Date",ascending=False),use_container_width=True)

st.download_button("⬇️ Download filtered CSV", f.to_csv(index=False), "filtered_retail_sales.csv", "text/csv")
