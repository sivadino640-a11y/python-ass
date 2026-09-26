students = [
    ["Siva", 80, 75, 90],
    ["Ravi", 70, 85, 80],
    ["Kiran", 90, 95, 85]
]

for student in students:
    name = student[0]
    marks = student[1:]

    total = sum(marks)
    average = total / len(marks)

    print("Name:", name)
    print("Total:", total)
    print("Average:", average)
    print()