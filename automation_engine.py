# PureFuel Automation Engine

# List of food products
products = [
    {"name": "Ultra-Processed Health Bar", "sugar": 20},
    {"name": "Apple & Almonds", "sugar": 6},
    {"name": "Sweetened Protein Yogurt", "sugar": 15}
]

# Expert threshold: flag products with 12g or more of sugar
for product in products:
    print(f"Analyzing {product['name']}...")

    if product["sugar"] >= 12:
        print("WARNING: This product has a high sugar content.")
    else:
        print("No high-sugar warning detected.")

    print()