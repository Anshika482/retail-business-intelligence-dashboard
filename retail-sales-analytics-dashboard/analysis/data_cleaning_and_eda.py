import pandas as pd

RAW_PATH = "data/retail_sales.csv"

df = pd.read_csv(RAW_PATH)

print("=== DATA QUALITY CHECK ===")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nDuplicate Order IDs:", df["Order_ID"].duplicated().sum())

df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")

df["Profit_Margin"] = (df["Profit"] / df["Revenue"].replace(0, pd.NA) * 100).round(2)
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

print("\n=== DESCRIPTIVE STATISTICS ===")
print(df[["Quantity","Unit_Price","Discount","Revenue","Profit"]].describe())

print("\n=== BUSINESS SUMMARY ===")
print("Revenue:", round(df["Revenue"].sum(),2))
print("Profit:", round(df["Profit"].sum(),2))
print("Orders:", df["Order_ID"].nunique())
print("Average Order Value:", round(df["Revenue"].sum()/df["Order_ID"].nunique(),2))
