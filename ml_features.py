import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/inventory_sales_features.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort by product and date
df = df.sort_values(["product_id", "date"])

# Create lag features
df["lag_1"] = df.groupby("product_id")["units_sold"].shift(1)
df["lag_7"] = df.groupby("product_id")["units_sold"].shift(7)
df["lag_14"] = df.groupby("product_id")["units_sold"].shift(14)

# Create rolling averages
df["rolling_7"] = (
    df.groupby("product_id")["units_sold"]
    .transform(lambda x: x.shift(1).rolling(7).mean())
)

df["rolling_30"] = (
    df.groupby("product_id")["units_sold"]
    .transform(lambda x: x.shift(1).rolling(30).mean())
)

# Remove rows with missing forecasting features
df = df.dropna(
    subset=[
        "lag_1",
        "lag_7",
        "lag_14",
        "rolling_7",
        "rolling_30"
    ]
)

# Save cleaned dataset
df.to_csv("data/raw/ml_features_clean.csv", index=False)

# Display results
print("Lag and rolling features created successfully!")
print()
print("Missing feature rows removed successfully!")
print("Remaining rows:", len(df))
print()

print(df[
    [
        "date",
        "product_id",
        "product_name",
        "units_sold",
        "lag_1",
        "lag_7",
        "lag_14",
        "rolling_7",
        "rolling_30"
    ]
].head(20))

print()
print("Saved as: data/raw/ml_features_clean.csv")