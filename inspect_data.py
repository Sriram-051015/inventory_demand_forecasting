import pandas as pd

df = pd.read_csv("data/raw/train.csv")

print("========== BASIC INFORMATION ==========")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

print("\n========== DATE INFORMATION ==========")
print("First date:", df["date"].min())
print("Last date:", df["date"].max())

print("\n========== STORES & PRODUCTS ==========")
print("Number of stores:", df["store"].nunique())
print("Number of products:", df["item"].nunique())

print("\n========== SALES STATISTICS ==========")
print(df["sales"].describe())