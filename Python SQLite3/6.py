import sqlite3

conn=sqlite3.connect("college.db")

cur=conn.cursor()

p=conn.execute("select *from students where marks>75")

for x in p:
    print(x)


