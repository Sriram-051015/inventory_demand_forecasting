import pandas as pd


# Load future inventory plan
df = pd.read_csv(
    "data/raw/future_inventory_plan.csv"
)


# Select dashboard columns
dashboard = df[
    [
        "product_id",
        "product_name",
        "category",
        "lead_time_days",
        "reorder_point",
        "average_daily_demand",
        "total_forecast_demand",
        "maximum_daily_demand",
        "lead_time_demand",
        "safety_stock",
        "recommended_stock_level",
        "inventory_action"
    ]
].copy()


# Rename columns for Power BI
dashboard = dashboard.rename(
    columns={
        "lead_time_days": "Lead Time Days",
        "reorder_point": "Reorder Point",
        "average_daily_demand": "Average Daily Demand",
        "total_forecast_demand": "30 Day Forecast Demand",
        "maximum_daily_demand": "Maximum Daily Demand",
        "lead_time_demand": "Lead Time Demand",
        "safety_stock": "Safety Stock",
        "recommended_stock_level": "Recommended Stock Level",
        "inventory_action": "Demand Category"
    }
)


# Save dashboard dataset
dashboard.to_csv(
    "powerbi/inventory_dashboard.csv",
    index=False
)


print("Power BI dashboard dataset created successfully!")
print()

print("Rows:", len(dashboard))
print("Columns:", len(dashboard.columns))
print()

print(dashboard.to_string(index=False))

print()

print(
    "Saved as: powerbi/inventory_dashboard.csv"
)