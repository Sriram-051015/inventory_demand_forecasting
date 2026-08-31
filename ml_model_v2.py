import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv("data/raw/train.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(["store", "item", "date"])

# Time features
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["day_of_week"] = df["date"].dt.dayofweek
df["week_of_year"] = df["date"].dt.isocalendar().week.astype(int)

# Lag features
group = df.groupby(["store", "item"])["sales"]

df["lag_1"] = group.shift(1)
df["lag_7"] = group.shift(7)
df["lag_14"] = group.shift(14)

# Rolling features
df["rolling_7"] = (
    group.shift(1)
    .rolling(7)
    .mean()
)

df["rolling_30"] = (
    group.shift(1)
    .rolling(30)
    .mean()
)

# Remove missing values
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
    "lag_1",
    "lag_7",
    "lag_14",
    "rolling_7",
    "rolling_30"
]

X_train = train[features]
y_train = train["sales"]

X_validation = validation[features]
y_validation = validation["sales"]

# Random Forest
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)

print("Training improved Random Forest model...")

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_validation)

# Evaluation
mae = mean_absolute_error(y_validation, predictions)

print()
print("Improved Random Forest completed!")
print("Validation MAE:", round(mae, 2))
print()
print("Previous Random Forest MAE: 7.92")