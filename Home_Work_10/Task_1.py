import sqlite3

conn = sqlite3.connect("AnimalKingdom.db")
cursor = conn.cursor()

try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Animals (
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        name_animal TEXT,
        type_animal TEXT
        )
    ''')

    list1 = [("Lion", 'mammal'), ("Crocodile", 'reptile'), ("Eagle", 'bird'),
             ("Sea turtle", 'reptile'), ("Monkey", 'mammal')]

    cursor.executemany("INSERT INTO Animals (name_animal, type_animal) VALUES (?, ?)", list1)
    conn.commit()

    cursor.execute(("UPDATE Animals SET name_animal = 'Falcon' WHERE name_animal = 'Eagle'"))
    conn.commit()

    print("\n Mammals:")
    cursor.execute("SELECT * FROM Animals WHERE type_animal = 'mammal'")
    mammals = cursor.fetchall()
    for m in mammals:
        print(m)

    print("\n All animals now:")
    cursor.execute("SELECT * FROM Animals")
    animal = cursor.fetchall()
    for a in animal:
        print(a)

finally:
    conn.close()
