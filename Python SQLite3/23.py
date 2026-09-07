import sqlite3

try:
    db = sqlite3.connect("college.db")
    c = db.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS student(
            id INTEGER,
            name TEXT,
            age INTEGER
        )
    """)

    while True:
        print("\n1. Insert")
        print("2. Display")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        try:
            ch = int(input("Enter choice: "))

            if ch == 1:
                id = int(input("Enter ID: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))

                c.execute(
                    "INSERT INTO student VALUES (?, ?, ?)",
                    (id, name, age)
                )
                db.commit()
                print("Inserted")

            elif ch == 2:
                c.execute("SELECT * FROM student")

                for row in c.fetchall():
                    print(row)

            elif ch == 3:
                id = int(input("Enter ID: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))

                c.execute(
                    "UPDATE student SET name = ?, age = ? WHERE id = ?",
                    (name, age, id)
                )
                db.commit()
                print("Updated")

            elif ch == 4:
                id = int(input("Enter ID: "))

                c.execute(
                    "DELETE FROM student WHERE id = ?",
                    (id,)
                )
                db.commit()
                print("Deleted")

            elif ch == 5:
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Enter numbers only.")

        except sqlite3.Error as e:
            print("Database error:", e)

except sqlite3.Error as e:
    print("Database connection error:", e)

finally:
    db.close()
