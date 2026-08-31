import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/inventory_records.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Create time-based features
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["day_of_week"] = df["date"].dt.dayofweek
df["week_of_year"] = df["date"].dt.isocalendar().week.astype(int)
df["quarter"] = df["date"].dt.quarter

# Weekend indicator
df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)

# Display result
print("\nTime-based features created successfully!\n")
print(df.head())

print("\nNew columns:")
print(df.columns.tolist())

# Save the new dataset
df.to_csv("data/raw/inventory_sales_features.csv", index=False)

print("\nSaved as: data/raw/inventory_sales_features.csv")