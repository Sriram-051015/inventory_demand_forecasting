import pandas as pd
import joblib
import os
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error


# Load cleaned dataset
df = pd.read_csv("data/raw/ml_features_clean.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(["product_id", "date"])


# Split date
split_date = df["date"].quantile(0.8)

train = df[df["date"] < split_date]
test = df[df["date"] >= split_date]


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


# Input and target
X_train = train[features]
y_train = train["units_sold"]

X_test = test[features]
y_test = test["units_sold"]


# Train Random Forest model
print("Training Random Forest model...")

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

print("Model training completed!")
print()


# Make predictions
predictions = model.predict(X_test)


# Calculate performance
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("Model Performance")
print("-----------------")
print("MAE :", round(mae, 2))
print("RMSE:", round(rmse, 2))


# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)


# Save trained model
joblib.dump(model, "models/inventory_demand_model.pkl")

print()
print("Model saved successfully!")
print("Saved as: models/inventory_demand_model.pkl")