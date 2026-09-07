import sqlite3

conn=sqlite3.connect("college.db")

cur=conn.cursor()

d=[(231,'shiva',18,'cme',82),
   (235,'vivek',17,'cme',70),
   (234,'mahesh',18,'cme',85),
   (236,'varun',18,'cme',90),
   (217,'teja',18,'cme',95)
]
conn.executemany(
    "insert into students values(?,?,?,?,?)",d
)

conn.commit()

conn.close()