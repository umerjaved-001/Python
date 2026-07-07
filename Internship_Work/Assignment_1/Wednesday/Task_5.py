# Write a program that determines the ticket category (Child, Student, Adult) based on age.
# Task 5

age = int(input("Enter your age:"))

if age < 10 :
    print("You have a child ticket.")
elif age < 20 :
    print("You have a student ticket.")
else :
    print("YOu have a adult ticket.")