import sqlite3

conn = sqlite3.connect("college.db")
cur = conn.cursor()

cur.execute("SELECT * FROM students WHERE name LIKE 'A%'")

for row in cur.fetchall():
    print(row)

conn.close()