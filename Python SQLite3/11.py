import sqlite3

conn=sqlite3.connect("college.db")

cur=conn.cursor()

d=[(101,'karthik',18,'python',82),
   (102,'vivek',17,'java',70),
   (103,'mahesh',18,'python',85),
   (104,'varun',18,'cme',90),
   (105,'teja',18,'cme',95),
   (106,'ram teja',18,'python',82),
   (107,'suresh',17,'java',70),
   (108,'revanth',18,'python',85),
   (109,'ashik',18,'cme',90),
   (110,'ganesh',18,'cme',95)
]
conn.executemany(
    "insert into students values(?,?,?,?,?)",d
)

conn.commit()

conn.close()