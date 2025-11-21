import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price TEXT,
        availability TEXT
    )
''')
conn.commit()

url = "https://books.toscrape.com/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
web = BeautifulSoup(response.text, "html.parser")

books = web.find_all("article", class_="product_pod")

for b in books:
    title = b.h3.a["title"]
    price = b.find("p", class_="price_color").text
    avail = b.find("p", class_="instock availability").text.strip()

    print(title, price, avail)

    cursor.execute(
        "INSERT INTO Books (title, price, availability) VALUES (?, ?, ?)",
        (title, price, avail)
    )

conn.commit()

cursor.execute("SELECT * FROM Books")
rows = cursor.fetchall()
print("\n=== Дані з БД ===")
for row in rows:
    print(row)

conn.close()
