import sqlite3

conn=sqlite3.connect("college.db")

cur=conn.cursor()

conn.execute("""
create table students(
id integer,
name text,
age integer,
course text,
marks integer
)
""")

conn.commit()
conn.close()
