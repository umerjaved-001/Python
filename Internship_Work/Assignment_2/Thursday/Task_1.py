def grade(marks):
    if marks < 0 or marks > 100:
        raise ValueError("marks must be between 0 and 100")
    if marks >= 90:
        return "A"
    if marks >= 80:
        return "B"
    if marks >= 70:
        return "C"
    if marks >= 60:
        return "D"
    return "F"

marks = int(input("Enter your Marks:"))
print(grade(marks))