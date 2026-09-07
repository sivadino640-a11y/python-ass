import sqlite3

conn=sqlite3.connect("college.db")

cur=conn.cursor()

z=conn.execute(
    "select *from students order by marks desc"
)

for x in z:
    print(x)