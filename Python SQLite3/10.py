import sqlite3

conn=sqlite3.connect("college.db")

cur=conn.cursor()

z=conn.execute(
    "delete from students where id=236"
)
cur.execute("select * from students")
for x in z:
    print(x)

conn.commit()