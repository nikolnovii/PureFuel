from search_engine import load_products, search_products, sort_products

# Initial state of the user
stats = {
    "blood_sugar": 0,
    "energy": 80,
    "money": 0.0
}


def display_dashboard():
    """Displays the user's current metrics."""
    print("\n--- PureFuel Health & Spending Dashboard ---")
    print(f"Blood Sugar Impact: {stats['blood_sugar']}/10")
    print(f"Energy Level: {stats['energy']}%")
    print(f"Total Money Spent: ${stats['money']:.2f}")
    print("---------------------------------------------")


def process_choice(product):
    """Updates the dashboard using a Product object."""
    stats["blood_sugar"] = min(
        10, max(0, stats["blood_sugar"] + product.spike_delta)
    )

    stats["energy"] = min(
        100, max(0, stats["energy"] + product.energy_delta)
    )

    stats["money"] += product.cost

    print(f"\nAnalyzing: {product.name}")
    print("Analysis complete.")

    if stats["blood_sugar"] >= 7 and stats["energy"] < 60:
        print("WARNING: High blood sugar impact and low energy detected.")
    elif stats["blood_sugar"] >= 7 or stats["energy"] < 60:
        print("NOTICE: One potential concern has been detected.")
    else:
        print("No major concerns detected.")

    print(f"Sugar content: {product.sugar_content}g")
    print(f"Processing level: {product.processed_level}/10")


def search_ingredients(products):
    """Searches the product database for an ingredient."""
    ingredient = input("Enter an ingredient to search for: ").strip()

    if not ingredient:
        print("WARNING: The ingredient field cannot be blank.")
        return

    matches, search_time = search_products(products, ingredient)

    if matches:
        print("\nIngredient found in:")
        for name in matches:
            print(f"- {name}")
    else:
        print("\nIngredient not found.")

    print(f"Search completed in {search_time:.8f} seconds.")


def show_sorted_products(products):
    """Displays products sorted by sugar content."""
    sorted_list = sort_products(products)

    print("\n--- Products Sorted by Sugar Content ---")

    for product in sorted_list:
        print(f"{product.name}: {product.sugar_content}g sugar")


def main():
    # Load product objects from external data storage
    try:
        products = load_products()
    except (FileNotFoundError, json.JSONDecodeError):
        print("ERROR: Could not load products.json.")
        return
    except KeyError as error:
        print(f"ERROR: Product data is missing {error}.")
        return

    print("Welcome to PureFuel.")
    print("Analyze food choices, ingredients, energy, and spending.")

    while True:
        display_dashboard()

        print("\nPlease select an option:")
        print("1. Ultra-Processed Health Bar")
        print("2. Apple & Almonds")
        print("3. Fast Food Value Meal")
        print("4. Search for an ingredient")
        print("5. Sort products by sugar content")
        print("6. Exit")

        raw_choice = input("Enter your selection (1-6): ").strip()

        # Handle empty input before converting to an integer
        if raw_choice == "":
            print("WARNING: Please enter a selection.")
            continue

        # Convert the input and handle letters or other invalid data
        try:
            choice = int(raw_choice)
        except ValueError:
            print("WARNING: Invalid input. Please enter a number from 1 to 6.")
            continue

        if choice in (1, 2, 3):
            process_choice(products[choice - 1])

        elif choice == 4:
            search_ingredients(products)

        elif choice == 5:
            show_sorted_products(products)

        elif choice == 6:
            print("\nThank you for using PureFuel.")
            print("Your food and spending analysis is complete.")
            break

        else:
            print("WARNING: Please choose a number from 1 to 6.")


if __name__ == "__main__":
    import json
    main()