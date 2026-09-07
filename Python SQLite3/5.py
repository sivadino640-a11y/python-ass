import sqlite3

conn=sqlite3.connect("college.db")

cur=conn.cursor()

rows=conn.execute("select name from students")

for row in rows:
    print(row)