import pandas as pd

# Load cleaned feature dataset
df = pd.read_csv("data/raw/ml_features_clean.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort by product and date
df = df.sort_values(["product_id", "date"])

# Find the date used for the split
split_date = df["date"].quantile(0.8)

# Split chronologically
train = df[df["date"] < split_date]
test = df[df["date"] >= split_date]

print("Data preparation completed!")
print()

print("Split date:", split_date.date())
print()

print("Training data:")
print(train.shape)

print()

print("Testing data:")
print(test.shape)

print()

print("Training period:")
print(train["date"].min(), "to", train["date"].max())

print()

print("Testing period:")
print(test["date"].min(), "to", test["date"].max())