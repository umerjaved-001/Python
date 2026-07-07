# Write a program that calculates a student's total marks, average marks, and pass/fail status.

# Task 1

Sub_1 = input("Enter the marks of first subject(Out of 100):")
Sub_2 = input("Enter the marks of second subject(Out of 100):")
Sub_3 = input("Enter the marks of third subject(Out of 100):")
Sub_4 = input("Enter the marks of fourth subject(Out of 100):")

total_marks = float(Sub_1) + float(Sub_2) + float(Sub_3) + float(Sub_4)
avg_marks = float(total_marks)/4
print("\n---Report Card---")
print("Total Marks(Out of 400):",total_marks)
print("Average Marks:",avg_marks)
if total_marks > 260:
    print("Congratulations, You have passed the exam.")
else:
    print("Unfortunatly, You have failed the exam.")