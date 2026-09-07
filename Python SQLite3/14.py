import sqlite3

conn=sqlite3.connect("college.db")

cur=conn.cursor()

p=conn.execute(
    "select count(*) from students"
)

for x in p:
    print(x)