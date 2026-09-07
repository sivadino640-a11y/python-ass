import sqlite3

conn=sqlite3.connect("college.db")

cur=conn.cursor()

z=conn.execute(
    "update students set marks=90 where id=235"
)
cur.execute("select * from students")
for x in z:
    print(x)

conn.commit()