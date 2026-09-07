import sqlite3

conn=sqlite3.connect("college.db")

cur=conn.cursor()

conn=conn.execute("select *from students")

for row in conn:
    print(row)