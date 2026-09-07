import sqlite3

conn=sqlite3.connect("college.db")

cur=conn.cursor()

p=conn.execute(
    "select course,count(*)from students group by course"
)

for x in p:
    print(x)