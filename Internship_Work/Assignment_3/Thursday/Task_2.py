cars = {
    "car1": {
        "Brand": "Toyota",
        "Model": "Camry",
        "Price": 25000
    },
    "car2": {
        "Brand": "Honda",
        "Model": "Civic",
        "Price": 23000
    },
    "car3": {
        "Brand": "BMW",
        "Model": "X5",
        "Price": 65000
    }
}

for car_key, car_details in cars.items():
    print(f"\n{car_key}:")
    for key, value in car_details.items():
        print(f"  {key}: {value}")