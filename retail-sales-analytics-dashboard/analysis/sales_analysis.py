import pandas as pd

df = pd.read_csv("data/retail_sales.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("Shape:", df.shape)
print("\nRevenue:", round(df["Revenue"].sum(),2))
print("Profit:", round(df["Profit"].sum(),2))
print("Orders:", df["Order_ID"].nunique())

print("\nRevenue by Region:")
print(df.groupby("Region")["Revenue"].sum().sort_values(ascending=False))

print("\nTop Products:")
print(df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(10))
