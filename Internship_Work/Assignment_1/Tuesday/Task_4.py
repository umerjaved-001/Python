# Write a program that determines whether a student is eligible for a scholarship based on
# CGPA and attendance.

# Task 4

attendance = input("Enter your attendance percentage: ")
cgpa = input("Enter your CGPA: ")

if float(attendance) >= 85 and float(cgpa) >= 3.5:
    print("You are eligible for the scholarship.")
else:
    print("You are not eligible for the scholarship.")