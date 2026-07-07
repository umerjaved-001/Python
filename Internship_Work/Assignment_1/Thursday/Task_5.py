# Write a program that determines scholarship status (Full Scholarship, Partial Scholarship, or
# Not Eligible) using CGPA, attendance, and family income.

# Task 5

cgpa = float(input("Enter your CGPA:"))
attendence = float(input("Enter your Attendence Persentage:"))
family_income = float(input("Enter yout Family Income:"))

if cgpa > 3.75 and attendence > 90 and family_income > 50000:
    print("Congratulations, You are Eligible for Fully Funded Scholarship.")
elif cgpa > 3.75 and attendence > 90 and family_income < 50000:
    print("Congratulations, You are Eligible for Fully Funded Scholarship.")
elif cgpa > 3.5 and attendence > 80 and family_income > 70000:
    print("Congratulations, You are Eligible for Partial Scholarship.")
elif cgpa > 3.5 and attendence > 80 and family_income < 70000:
    print("Congratulations, You are Eligible for Partial Scholarship.")
elif cgpa < 3.5 and attendence < 80 and family_income > 70000:
    print("Sorry, You are not eligible for Scholarship.")
else:
    print("Sorry, You are not eligible for Scholarship.")