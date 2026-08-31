import pandas as pd


# Load future inventory plan
df = pd.read_csv("data/raw/future_inventory_plan.csv")


# Basic statistics
total_products = df["product_id"].nunique()

total_forecast_demand = df["total_forecast_demand"].sum()

total_recommended_stock = df["recommended_stock_level"].sum()


# Highest demand products
highest_demand = df.nlargest(
    5,
    "average_daily_demand"
)[
    [
        "product_id",
        "product_name",
        "average_daily_demand"
    ]
]


# Highest stock requirement
highest_stock_requirement = df.nlargest(
    5,
    "recommended_stock_level"
)[
    [
        "product_id",
        "product_name",
        "recommended_stock_level"
    ]
]


# Demand category summary
demand_categories = (
    df["inventory_action"]
    .value_counts()
    .reset_index()
)

demand_categories.columns = [
    "demand_category",
    "product_count"
]


# Create report
report = []

report.append("INVENTORY DEMAND FORECASTING REPORT")
report.append("=" * 45)
report.append("")

report.append("1. PROJECT SUMMARY")
report.append("-" * 30)
report.append(
    f"Products analyzed: {total_products}"
)
report.append(
    f"Forecast period: 30 days"
)
report.append(
    f"Total forecast demand: "
    f"{total_forecast_demand:.2f} units"
)
report.append(
    f"Total recommended stock: "
    f"{total_recommended_stock:.2f} units"
)
report.append("")


report.append("2. HIGHEST DEMAND PRODUCTS")
report.append("-" * 30)

for _, row in highest_demand.iterrows():

    report.append(
        f"{row['product_name']}: "
        f"{row['average_daily_demand']:.2f} units/day"
    )

report.append("")


report.append("3. HIGHEST STOCK REQUIREMENTS")
report.append("-" * 30)

for _, row in highest_stock_requirement.iterrows():

    report.append(
        f"{row['product_name']}: "
        f"{row['recommended_stock_level']:.2f} units"
    )

report.append("")


report.append("4. DEMAND CATEGORY SUMMARY")
report.append("-" * 30)

for _, row in demand_categories.iterrows():

    report.append(
        f"{row['demand_category']}: "
        f"{row['product_count']} products"
    )

report.append("")


report.append("5. RECOMMENDATIONS")
report.append("-" * 30)

report.append(
    "• Maintain higher inventory levels for high-demand products."
)

report.append(
    "• Monitor products with high lead-time demand."
)

report.append(
    "• Keep safety stock to reduce the risk of stockouts."
)

report.append(
    "• Review reorder levels regularly using updated forecasts."
)

report.append(
    "• Prioritize Notebook, Ballpoint Pen Pack, "
    "Sticky Notes and Toothbrush Pack because "
    "they have the highest predicted demand."
)

report.append("")


# Save report
report_text = "\n".join(report)

with open(
    "data/raw/inventory_report.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(report_text)


# Display report
print(report_text)

print()
print("Inventory report generated successfully!")
print("Saved as: data/raw/inventory_report.txt")