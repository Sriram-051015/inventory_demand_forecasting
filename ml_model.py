import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv("data/raw/train.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(["store", "item", "date"])

# Create time features
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["day_of_week"] = df["date"].dt.dayofweek
df["week_of_year"] = df["date"].dt.isocalendar().week.astype(int)

# Create previous-day sales
df["previous_sales"] = df.groupby(
    ["store", "item"]
)["sales"].shift(1)

# Remove rows without previous sales
df = df.dropna()

# Split data
train = df[df["date"] < "2017-01-01"]
validation = df[df["date"] >= "2017-01-01"]

# Features
features = [
    "store",
    "item",
    "year",
    "month",
    "day",
    "day_of_week",
    "week_of_year",
    "previous_sales"
]

X_train = train[features]
y_train = train["sales"]

X_validation = validation[features]
y_validation = validation["sales"]

# Create model
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)

# Train
print("Training Random Forest model...")
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_validation)

# Evaluate
mae = mean_absolute_error(y_validation, predictions)

print()
print("Random Forest model completed!")
print("Validation MAE:", round(mae, 2))
print()
print("Baseline MAE: 11.24")