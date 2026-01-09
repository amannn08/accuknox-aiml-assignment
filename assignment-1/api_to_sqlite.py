import requests
import sqlite3
import os

api_url = "https://jsonplaceholder.typicode.com/posts"
db_path = os.path.join("assignment-1", "databases", "books.db")

# fetch data from api
response = requests.get(api_url)
data = response.json()

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER
)
""")

# insert a few records (api does not give author/year, so assumed)
for item in data[:10]:
    title = item["title"]
    author = "Author " + str(item["userId"])
    year = 2020 + (item["id"] % 3)

    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (title, author, year)
    )

conn.commit()

cursor.execute("SELECT title, author, year FROM books")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
