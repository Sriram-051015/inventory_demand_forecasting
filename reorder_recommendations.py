import pandas as pd

# Load demand predictions
df = pd.read_csv("data/raw/demand_predictions.csv")

# Calculate demand during lead time
df["lead_time_demand"] = (
    df["predicted_demand"] * df["lead_time_days"]
)

# Calculate safety stock
df["safety_stock"] = (
    df["rolling_7"] * 0.5
)

# Calculate recommended stock level
df["recommended_stock"] = (
    df["lead_time_demand"] + df["safety_stock"]
)

# Decide whether to reorder
df["reorder_recommendation"] = df.apply(
    lambda row:
    "REORDER"
    if row["closing_stock"] < row["recommended_stock"]
    else "NO REORDER",
    axis=1
)

# Calculate reorder quantity
df["reorder_quantity"] = (
    df["recommended_stock"] - df["closing_stock"]
).clip(lower=0)

# Round values
df["lead_time_demand"] = df["lead_time_demand"].round(2)
df["safety_stock"] = df["safety_stock"].round(2)
df["recommended_stock"] = df["recommended_stock"].round(2)
df["reorder_quantity"] = df["reorder_quantity"].round(0)

# Save recommendations
df.to_csv(
    "data/raw/inventory_reorder_recommendations.csv",
    index=False
)

# Display results
print("Reorder recommendations generated successfully!")
print()

print(
    df[
        [
            "date",
            "product_id",
            "product_name",
            "closing_stock",
            "predicted_demand",
            "lead_time_days",
            "reorder_point",
            "recommended_stock",
            "reorder_quantity",
            "reorder_recommendation"
        ]
    ].head(20)
)

print()
print("Saved as: data/raw/inventory_reorder_recommendations.csv")