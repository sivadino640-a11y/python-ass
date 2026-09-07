import sqlite3

conn = sqlite3.connect("college.db")
cur = conn.cursor()

cur.execute("SELECT * FROM students WHERE marks BETWEEN 60 AND 90")

for row in cur.fetchall():
    print(row)

conn.close()