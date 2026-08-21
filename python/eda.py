print("EDA Started")

import pandas as pd

# Load cleaned sales data
df = pd.read_csv("../data/cleaned_sales_data.csv")

print("Dataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nDescriptive Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum())

print("\nTop Products:")
print(
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
