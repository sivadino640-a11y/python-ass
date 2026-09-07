import sqlite3

class Database:

    def __init__(self):
        self.db = sqlite3.connect("college.db")
        self.c = self.db.cursor()

    # CREATE
    def insert_student(self, id, name, age):
        try:
            self.c.execute(
                "INSERT INTO students VALUES (?, ?, ?)",
                (id, name, age)
            )
            self.db.commit()
            print("Student inserted")

        except sqlite3.Error as e:
            self.db.rollback()
            print("Error:", e)

    # READ
    def display_students(self):
        try:
            self.c.execute("SELECT * FROM students")

            for row in self.c.fetchall():
                print(row)

        except sqlite3.Error as e:
            print("Error:", e)

    # UPDATE
    def update_student(self, id, name, age):
        try:
            self.c.execute(
                "UPDATE students SET name=?, age=? WHERE student_id=?",
                (name, age, id)
            )
            self.db.commit()
            print("Student updated")

        except sqlite3.Error as e:
            self.db.rollback()
            print("Error:", e)

    # DELETE
    def delete_student(self, id):
        try:
            self.c.execute(
                "DELETE FROM students WHERE student_id=?",
                (id,)
            )
            self.db.commit()
            print("Student deleted")

        except sqlite3.Error as e:
            self.db.rollback()
            print("Error:", e)

    def close(self):
        self.db.close()


# Create object
db = Database()

# CRUD operations
db.insert_student(1, "Rahul", 20)
db.display_students()
db.update_student(1, "Rahul Kumar", 21)
db.delete_student(1)

db.close()
