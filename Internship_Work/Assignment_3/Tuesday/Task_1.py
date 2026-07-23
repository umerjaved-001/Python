students = []
for i in range(1, 6):
    name = input(f"Enter student name {i}: ")
    students.append(name)

print("\nStudent names:")
for student in students:
    print(student)
