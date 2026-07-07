# Write a program that determines whether an employee qualifies for a bonus based on salary
# and years of experience.

# Task 3

salary = float(input("Enter your salary:"))
year_of_exp =int(input("Enter your years of experience:"))

if salary >= 50000 and year_of_exp > 5:
    print("Congratulation, You have qualified for bonus.")
else:
    print("You didnot qualify for bonus.")
