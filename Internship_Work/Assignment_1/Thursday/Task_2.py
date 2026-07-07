# Write a program that checks whether a student is eligible for university admission based on
# age and intermediate percentage.

# Task 2

age = int(input("Enter you age:"))
inter_per = float(input("Enter your intermediate Persentage:"))

if age >= 18 and inter_per > 70:
    print("You are eligible for university admission.")
else :
    print("You are not eligibile for university admission.")
