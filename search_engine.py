import json
import time
from models import Product


def load_products(filename="products.json"):
    """Loads product data and creates Product objects."""
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [Product.from_dict(item) for item in data]


def search_products(products, search_item):
    """Finds products containing a specific ingredient."""
    start_time = time.perf_counter()
    search_item = search_item.strip().lower()

    matches = []

    for product in products:
        for ingredient in product.ingredients:
            if search_item in ingredient.lower():
                matches.append(product.name)
                break

    search_time = time.perf_counter() - start_time
    return matches, search_time


def sort_products(products):
    """Sorts products from lowest to highest sugar content."""
    return sorted(
        products,
        key=lambda product: product.sugar_content
    )