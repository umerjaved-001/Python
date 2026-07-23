# Dictionary of five products with Name, Price, and Stock
products = {
    "Product1": {
        "Name": "Laptop",
        "Price": 899.99,
        "Stock": 15
    },
    "Product2": {
        "Name": "Mouse",
        "Price": 29.99,
        "Stock": 50
    },
    "Product3": {
        "Name": "Keyboard",
        "Price": 79.99,
        "Stock": 30
    },
    "Product4": {
        "Name": "Monitor",
        "Price": 299.99,
        "Stock": 12
    },
    "Product5": {
        "Name": "Headphones",
        "Price": 149.99,
        "Stock": 25
    }
}

# Display every product and its details using nested loops
for product_id, product_details in products.items():
    print(f"\n{product_id}:")
    for key, value in product_details.items():
        print(f"  {key}: {value}")
