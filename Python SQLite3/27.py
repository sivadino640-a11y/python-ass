import sqlite3

db = sqlite3.connect("college.db")
c = db.cursor()

try:
    c.execute("""
    SELECT students.name, courses.course_name
    FROM enrollments
    JOIN students
    ON enrollments.student_id = students.student_id
    JOIN courses
    ON enrollments.course_id = courses.course_id
    """)

    for row in c.fetchall():
        print("Student:", row[0], "Course:", row[1])

except sqlite3.Error as e:
    print("Error:", e)

db.close()
