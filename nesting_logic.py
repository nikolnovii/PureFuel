# PureFuel Nesting Logic

# Each product contains a list of ingredients
products = [
    {
        "name": "Ultra-Processed Health Bar",
        "ingredients": ["oats", "sugar", "corn syrup", "palm oil"]
    },
    {
        "name": "Apple & Almonds",
        "ingredients": ["apple", "almonds"]
    },
    {
        "name": "Sweetened Protein Yogurt",
        "ingredients": ["milk", "sugar", "protein", "corn syrup"]
    }
]

print("PureFuel Nested Food Analysis")
print("-----------------------------")

# Outer loop: goes through each product
for product in products:
    print(f"\nAnalyzing: {product['name']}")

    # Inner loop: goes through each ingredient
    for ingredient in product["ingredients"]:
        if "sugar" in ingredient.lower() or "syrup" in ingredient.lower():
            print(f"  WARNING: Potential added sugar -> {ingredient}")
        else:
            print(f"  Checked: {ingredient}")

print("\nAnalysis complete.")