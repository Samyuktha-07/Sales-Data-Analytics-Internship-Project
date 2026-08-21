import pandas as pd

# Load cleaned data
df = pd.read_csv("../data/cleaned_sales_data.csv")

# Create dashboard KPIs
total_sales = df["Sales"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order_ID"].nunique()

print("Dashboard KPIs")
print("----------------------")
print("Total Sales:", total_sales)
print("Total Quantity:", total_quantity)
print("Total Orders:", total_orders)
