import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/train.csv")

df["date"] = pd.to_datetime(df["date"])

monthly_sales = df.groupby(
    df["date"].dt.to_period("M")
)["sales"].sum()

plt.figure(figsize=(14, 6))

plt.plot(monthly_sales.index.astype(str), monthly_sales.values)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=90)
plt.tight_layout()

plt.show()