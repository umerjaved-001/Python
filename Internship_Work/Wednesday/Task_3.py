# Write a program that assigns grades (A, B, C, D, F) according to marks entered by the user.

# Task 3 

marks = float(input("Enter your marks:"))

if marks >= 90:
    print("You have got A grade.")
elif marks >= 80:
    print("You have got B grade.")
elif marks >= 70:
    print("You have got C grade.")
elif marks >= 60:
    print("You have got D grade.")
else :
    print("You have got F grade.")