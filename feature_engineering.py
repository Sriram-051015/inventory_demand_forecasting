import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/train.csv")

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Create time-based features
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["day_of_week"] = df["date"].dt.dayofweek
df["week_of_year"] = df["date"].dt.isocalendar().week.astype(int)

print("Time features created successfully!")
print()
print(df.head())
print()
print("Columns:")
print(df.columns.tolist())