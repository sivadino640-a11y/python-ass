import sqlite3

db = sqlite3.connect("college.db")
c = db.cursor()

try:
    c.execute("""
    CREATE TABLE IF NOT EXISTS students(
        student_id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS courses(
        course_id INTEGER PRIMARY KEY,
        course_name TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS enrollments(
        enrollment_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_id INTEGER
    )
    """)

    db.commit()
    print("Tables created successfully.")

except sqlite3.Error as e:
    print("Error:", e)
    db.rollback()

db.close()