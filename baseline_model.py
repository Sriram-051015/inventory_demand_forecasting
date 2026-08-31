import pandas as pd
from sklearn.metrics import mean_absolute_error

# Load data
df = pd.read_csv("data/raw/train.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort correctly
df = df.sort_values(["store", "item", "date"])

# Previous day's sales
df["previous_sales"] = df.groupby(
    ["store", "item"]
)["sales"].shift(1)

# Keep only validation period
validation = df[df["date"] >= "2017-01-01"].copy()

# Remove rows where previous sales is unavailable
validation = validation.dropna(subset=["previous_sales"])

# Actual vs predicted
actual = validation["sales"]
predicted = validation["previous_sales"]

# Calculate MAE
mae = mean_absolute_error(actual, predicted)

print("Baseline model completed!")
print()
print("Validation MAE:", round(mae, 2))