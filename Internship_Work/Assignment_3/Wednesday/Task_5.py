countries = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasília",
    "Canada": "Ottawa",
    "Australia": "Canberra"
}

country = input("Enter a country name: ").strip()
capital = countries.get(country)

if capital:
    print(f"The capital of {country} is {capital}.")
else:
    print(f"{country} is not in the list.")
