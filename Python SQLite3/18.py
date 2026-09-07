import sqlite3

conn=sqlite3.connect("college.db")
cur=conn.cursor()

cur.execute(
    "SELECT course, AVG(marks) FROM students GROUP BY course"
    )

for row in cur.fetchall():
    print(row)

conn.close()