import sqlite3

conn=sqlite3.connect("college.db")

cur=conn.cursor()

row=conn.execute("select *from students where course=python")

for x in row:
    print(x)
