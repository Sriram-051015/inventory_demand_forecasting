import pandas as pd


# Load future demand forecast
df = pd.read_csv("data/raw/future_demand_forecast.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])


# Calculate average predicted daily demand
summary = (
    df.groupby(
        [
            "product_id",
            "product_name",
            "category",
            "lead_time_days",
            "reorder_point"
        ]
    )
    .agg(
        average_daily_demand=("predicted_demand", "mean"),
        total_forecast_demand=("predicted_demand", "sum"),
        maximum_daily_demand=("predicted_demand", "max")
    )
    .reset_index()
)


# Lead-time demand
summary["lead_time_demand"] = (
    summary["average_daily_demand"]
    * summary["lead_time_days"]
)


# Safety stock
summary["safety_stock"] = (
    summary["maximum_daily_demand"]
    - summary["average_daily_demand"]
) * summary["lead_time_days"]


# Prevent negative safety stock
summary["safety_stock"] = summary["safety_stock"].clip(lower=0)


# Recommended stock level
summary["recommended_stock_level"] = (
    summary["lead_time_demand"]
    + summary["safety_stock"]
)


# Round values
summary["average_daily_demand"] = (
    summary["average_daily_demand"].round(2)
)

summary["total_forecast_demand"] = (
    summary["total_forecast_demand"].round(2)
)

summary["maximum_daily_demand"] = (
    summary["maximum_daily_demand"].round(2)
)

summary["lead_time_demand"] = (
    summary["lead_time_demand"].round(2)
)

summary["safety_stock"] = (
    summary["safety_stock"].round(2)
)

summary["recommended_stock_level"] = (
    summary["recommended_stock_level"].round(2)
)


# Inventory recommendation
summary["inventory_action"] = summary.apply(
    lambda row:
    "HIGH DEMAND" if row["average_daily_demand"] > 40
    else "MEDIUM DEMAND" if row["average_daily_demand"] > 20
    else "LOW DEMAND",
    axis=1
)


# Sort by demand
summary = summary.sort_values(
    "average_daily_demand",
    ascending=False
)


# Save inventory plan
summary.to_csv(
    "data/raw/future_inventory_plan.csv",
    index=False
)


print("Future inventory plan generated successfully!")
print()

print("Products analyzed:", len(summary))

print()

print(summary.to_string(index=False))

print()

print("Saved as: data/raw/future_inventory_plan.csv")