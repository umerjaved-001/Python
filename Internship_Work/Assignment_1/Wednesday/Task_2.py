# Write a program that classifies weather as Hot, Moderate, or Cold based on temperature entered by the user.

# Task 2

temperature = float(input("Enter the temperature: "))

if temperature >= 35:
    print("Today, the weather is very Hot")
elif temperature >= 25:
    print("Today, the weather is Moderate")
else:
    print("Today, the weather is very Cold")