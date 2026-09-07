import sqlite3

db = sqlite3.connect("college.db")
c = db.cursor()
try:
    c.execute("BEGIN")

    c.execute(
        "INSERT INTO students VALUES (?, ?, ?)",
        (1, "Ravi", 20)
    )

    c.execute(
        "INSERT INTO students VALUES (?, ?, ?)",
        (2, "Priya", 21)
    )

    c.execute(
        "UPDATE students SET age = ? WHERE id = ?",
        (22, 2)
    )
    db.commit()
    print("All records saved successfully")

except sqlite3.Error as e:
    db.rollback()
    print("Error:", e)

db.close()
