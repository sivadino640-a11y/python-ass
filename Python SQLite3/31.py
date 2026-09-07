import sqlite3

db = sqlite3.connect("college.db")
c = db.cursor()

name = input("Enter name: ")
age = input("Enter age: ")

c.execute(
    "SELECT * FROM students WHERE name LIKE ? AND age = ?",
    ("%" + name + "%", age)
)

rows = c.fetchall()

if rows:
    for row in rows:
        print(row)
else:
    print("No student found")

db.close()
