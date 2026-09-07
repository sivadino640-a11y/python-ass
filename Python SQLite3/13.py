import sqlite3

conn=sqlite3.connect("college.db")

cur=conn.cursor()

abc = conn.execute(
    "select *from students order by marks desc limit 3"
)

for x in abc:
    print(x)