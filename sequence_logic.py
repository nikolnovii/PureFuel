# PureFuel Sequence Logic

# Ingredient sequence from a food product
ingredients = "oats,sugar,corn syrup,palm oil,almond flour"

print("PureFuel Ingredient Scanner")
print("----------------------------")

# Use an index to access the first ingredient
first_ingredient = ingredients.split(",")[0]
print(f"First ingredient: {first_ingredient}")

# Iterate through each ingredient
ingredient_list = ingredients.split(",")

print("\nScanning ingredients...")

for ingredient in ingredient_list:
    ingredient = ingredient.strip()

    if "sugar" in ingredient.lower() or "syrup" in ingredient.lower():
        print(f"WARNING: Potential added sugar found -> {ingredient}")
    else:
        print(f"Checked: {ingredient}")

print("\nScan complete.")