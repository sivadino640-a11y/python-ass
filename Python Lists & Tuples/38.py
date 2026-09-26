employees = [
    ("Siva", "Developer", 50000),
    ("Ravi", "Manager", 70000),
    ("Kiran", "Tester", 45000),
    ("Rahul", "Designer", 60000)
]

highest = employees[0]

for employee in employees:
    if employee[2] > highest[2]:
        highest = employee

print("Highest Salary Employee:")
print("Name:", highest[0])
print("Designation:", highest[1])
print("Salary:", highest[2])