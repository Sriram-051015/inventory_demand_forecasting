import pandas as pd

# Load reorder recommendations
df = pd.read_csv(
    "data/raw/inventory_reorder_recommendations.csv"
)

# Count reorder recommendations
reorder_counts = df["reorder_recommendation"].value_counts()

print("Reorder Analysis")
print("----------------")
print(reorder_counts)

print()

# Show products that need reorder
reorder_items = df[
    df["reorder_recommendation"] == "REORDER"
]

print("Total reorder records:", len(reorder_items))
print()

# Total reorder quantity
total_reorder_quantity = reorder_items[
    "reorder_quantity"
].sum()

print(
    "Total recommended reorder quantity:",
    int(total_reorder_quantity)
)

print()

# Product-level summary
product_summary = (
    reorder_items
    .groupby(
        ["product_id", "product_name"],
        as_index=False
    )
    .agg(
        reorder_count=("reorder_recommendation", "count"),
        total_reorder_quantity=("reorder_quantity", "sum")
    )
    .sort_values(
        "total_reorder_quantity",
        ascending=False
    )
)

print("Products requiring reorder:")
print(product_summary)

# Save analysis
product_summary.to_csv(
    "data/raw/reorder_summary.csv",
    index=False
)

print()
print("Saved as: data/raw/reorder_summary.csv")