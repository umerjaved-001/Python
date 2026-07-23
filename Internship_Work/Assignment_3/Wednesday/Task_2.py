laptop_specs = {
    "Brand": "Dell",
    "Processor": "Intel Core i7",
    "RAM": "16GB",
    "Storage": "512GB SSD",
    "Price": 1200
}

print("Original laptop specifications:")
for key, value in laptop_specs.items():
    print(f"{key}: {value}")

laptop_specs["RAM"] = "32GB"
laptop_specs["Color"] = "Silver"

print("\nUpdated laptop specifications:")
for key, value in laptop_specs.items():
    print(f"{key}: {value}")
