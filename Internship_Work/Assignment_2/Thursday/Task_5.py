def calculate_total(m1, m2, m3):
    return m1 + m2 + m3


def calculate_average(total):
    return total / 3


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 50:
        return "E"
    else:
        return "F"


def display_report(name, total, average, grade):
    print("--- RESULT ---")
    print("Student Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Grade:", grade)


name = input("Enter student name: ")
mark1 = int(input("Enter Subject 1 marks: "))
mark2 = int(input("Enter Subject 2 marks: "))
mark3 = int(input("Enter Subject 3 marks: "))

total_score = calculate_total(mark1, mark2, mark3)
average_score = calculate_average(total_score)
final_grade = calculate_grade(average_score)

display_report(name, total_score, average_score, final_grade)