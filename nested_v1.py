# PureFuel Nested Food Analyzer

products = [
    {
        "name": "Ultra-Processed Health Bar",
        "details": {
            "sugar": 20,
            "ingredients": ["oats", "sugar", "corn syrup", "palm oil"]
        }
    },
    {
        "name": "Apple & Almonds",
        "details": {
            "sugar": 6,
            "ingredients": ["apple", "almonds"]
        }
    },
    {
        "name": "Sweetened Protein Yogurt",
        "details": {
            "sugar": 15,
            "ingredients": ["milk", "sugar", "protein", "corn syrup"]
        }
    }
]

print("=== PureFuel Nested Food Analyzer ===")

# Outer loop: goes through each product
for product in products:
    print(f"\nProduct: {product['name']}")
    print(f"Sugar Content: {product['details']['sugar']}g")

    # Nested loop: goes through each ingredient
    print("Ingredients:")

    for ingredient in product["details"]["ingredients"]:
        if "sugar" in ingredient.lower() or "syrup" in ingredient.lower():
            print(f"  WARNING: {ingredient}")
        else:
            print(f"  - {ingredient}")

print("\nAnalysis complete.")