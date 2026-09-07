import sqlite3

db = sqlite3.connect("college.db")
c = db.cursor()

try:
    c.execute("""
    SELECT students.name
    FROM students
    LEFT JOIN enrollments
    ON students.student_id = enrollments.student_id
    WHERE enrollments.student_id IS NULL
    """)

    for row in c.fetchall():
        print("Student:", row[0])

except sqlite3.Error as e:
    print("Error:", e)

db.close()
