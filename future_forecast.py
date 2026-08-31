import pandas as pd
import joblib


# Load cleaned data
df = pd.read_csv("data/raw/ml_features_clean.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

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


# Get the latest record for every product
latest = (
    df.sort_values("date")
    .groupby("product_id")
    .tail(1)
    .copy()
)


# Number of future days
forecast_days = 30


future_rows = []


# Create future dates
for _, row in latest.iterrows():

    for i in range(1, forecast_days + 1):

        future_date = row["date"] + pd.Timedelta(days=i)

        new_row = row.copy()

        new_row["date"] = future_date

        future_rows.append(new_row)


# Create future dataframe
future = pd.DataFrame(future_rows)


# Create time features
future["year"] = future["date"].dt.year
future["month"] = future["date"].dt.month
future["day"] = future["date"].dt.day
future["day_of_week"] = future["date"].dt.dayofweek
future["week_of_year"] = (
    future["date"].dt.isocalendar().week.astype(int)
)
future["quarter"] = future["date"].dt.quarter
future["is_weekend"] = (
    future["day_of_week"] >= 5
).astype(int)


# Generate predictions
future["predicted_demand"] = model.predict(
    future[features]
)

future["predicted_demand"] = (
    future["predicted_demand"].round(2)
)


# Keep useful columns
future_forecast = future[
    [
        "date",
        "product_id",
        "product_name",
        "category",
        "predicted_demand",
        "lead_time_days",
        "reorder_point"
    ]
]


# Save future forecast
future_forecast.to_csv(
    "data/raw/future_demand_forecast.csv",
    index=False
)


print("Future demand forecast generated successfully!")
print()

print("Forecast period:")
print(
    future_forecast["date"].min(),
    "to",
    future_forecast["date"].max()
)

print()

print(
    "Number of forecast records:",
    len(future_forecast)
)

print()

print(future_forecast.head(20))

print()

print(
    "Saved as: data/raw/future_demand_forecast.csv"
)