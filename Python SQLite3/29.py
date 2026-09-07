import sqlite3

db = sqlite3.connect("college.db")
c = db.cursor()

try:
    c.execute("""
    SELECT courses.course_name, COUNT(enrollments.student_id)
    FROM courses
    LEFT JOIN enrollments
    ON courses.course_id = enrollments.course_id
    GROUP BY courses.course_id
    """)

    for row in c.fetchall():
        print("Course:", row[0], "Students:", row[1])

except sqlite3.Error as e:
    print("Error:", e)

db.close()
