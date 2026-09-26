students = [
    ("Siva", 85),
    ("Ravi", 75),
    ("Kiran", 90),
    ("Rahul", 80)
]

search_name = "Kiran"

found = False

for name, marks in students:
    if name == search_name:
        print("Student found")
        print("Name:", name)
        print("Marks:", marks)
        found = True
        break

if not found:
    print("Student not found")