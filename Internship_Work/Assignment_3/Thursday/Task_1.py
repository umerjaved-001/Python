phone = {
    "Brand": "Samsung",
    "Model": "Galaxy S21",
    "RAM": "8GB",
    "Storage": "128GB",
    "Battery": "4000mAh"
}

# Update one specification
phone["Storage"] = "256GB"

# Add Color
phone["Color"] = "Phantom Gray"

# Remove Battery
phone.pop("Battery", None)

# Display the final dictionary
print(phone)
