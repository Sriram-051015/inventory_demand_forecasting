import pandas as pd
import joblib

# Load cleaned dataset
df = pd.read_csv("data/raw/ml_features_clean.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(["product_id", "date"])

# Use the same split as training
split_date = df["date"].quantile(0.8)

test = df[df["date"] >= split_date].copy()

# Load trained model
model = joblib.load("models/inventory_demand_model.pkl")

# Features used by the model
features = [
    "year",
    "month",
    "day",
    "day_of_week",
    "week_of_year",
    "quarter",
    "is_weekend",
    "opening_stock",
    "stock_received",
    "closing_stock",
    "reorder_point",
    "lead_time_days",
    "lag_1",
    "lag_7",
    "lag_14",
    "rolling_7",
    "rolling_30"
]

# Generate predictions
test["predicted_demand"] = model.predict(test[features])

# Round predictions
test["predicted_demand"] = test["predicted_demand"].round(2)

# Save predictions
test.to_csv("data/raw/demand_predictions.csv", index=False)

print("Demand predictions generated successfully!")
print()
print("Number of predictions:", len(test))
print()
print(test[
    [
        "date",
        "product_id",
        "product_name",
        "units_sold",
        "predicted_demand"
    ]
].head(20))

print()
print("Saved as: data/raw/demand_predictions.csv")