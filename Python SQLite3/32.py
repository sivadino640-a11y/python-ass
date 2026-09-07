import sqlite3

db = sqlite3.connect("college.db")
c = db.cursor()

name = input("Enter name: ")

page = int(input("Enter page number: "))
limit = 5
offset = (page - 1) * limit

c.execute("""
SELECT * FROM students
WHERE name LIKE ?
LIMIT ? OFFSET ?
""", ("%" + name + "%", limit, offset))

rows = c.fetchall()

if rows:
    for row in rows:
        print(row)
else:
    print("No students found")

db.close()
