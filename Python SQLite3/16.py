import sqlite3

conn=sqlite3.connect("college.db")

cur=conn.cursor()

p=conn.execute(
    "select max(marks) min(marks) from students"
)

for x in p:
    print(x)