def calculate_average(total,n):
    average = total / n
    
    return average

total_subj  = int(input("Enter your total subjects: "))
total_marks = float(input("Enter your total marks: "))
Result = calculate_average(total_marks,total_subj)

print(f"The average marks are: {Result}")