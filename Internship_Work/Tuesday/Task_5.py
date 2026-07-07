# Write a program that checks whether a number is positive, negative, or zero.

# Task 5

Num = input("Enter a number(Positive/Negative/Zero): ")
if int(Num) > 0:
    print("The number is positive.")
elif int(Num) < 0:
    print("The number is negative.")
else:
    print("The number is zero.")