import pandas as pd

df = pd.read_csv("data/raw/train.csv")

print("Dataset loaded successfully!")
print()
print("Shape:", df.shape)
print()
print("Columns:")
print(df.columns)
print()
print("First 5 rows:")
print(df.head())