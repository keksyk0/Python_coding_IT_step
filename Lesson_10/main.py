import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
        )
    ''')

    list1 = [("Ivan", 25), ("Stefania", 15), ("Oleg", 14), ("Daniel", 54)]
    cursor.executemany("INSERT INTO students (name, age) VALUES (?, ?)", list1)
    conn.commit()

    cursor.execute("SELECT * FROM students")
    stud = cursor.fetchall()
    for s in stud:
        print(s)

finally:
    conn.close()

