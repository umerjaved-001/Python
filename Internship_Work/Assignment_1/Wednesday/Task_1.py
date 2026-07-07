# Write a program that compares two numbers and displays the larger number.

# Task 1

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

if float(num1) > float(num2):
    print("The larger number is: ", num1)
elif float(num1) < float(num2):
    print("The larger number is: ", num2)
else:
    print("Both numbers are equal.")