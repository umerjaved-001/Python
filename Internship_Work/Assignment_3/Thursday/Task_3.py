# Nested dictionary for three students
students = {
    "Student1": {
        "Age": 20,
        "Department": "Computer Science",
        "CGPA": 3.85
    },
    "Student2": {
        "Age": 21,
        "Department": "Electronics",
        "CGPA": 3.72
    },
    "Student3": {
        "Age": 19,
        "Department": "Mechanical",
        "CGPA": 3.92
    }
}

# Display all student information using nested loops
for student_name, details in students.items():
    print(f"\n{student_name}:")
    for key, value in details.items():
        print(f"  {key}: {value}")