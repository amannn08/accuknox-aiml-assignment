import csv
import sqlite3
import os


db_path = os.path.join("assignment-1", "databases", "users.db")
csv_path = os.path.join("assignment-1", "data", "users.csv")


conn = sqlite3.connect(db_path)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")


with open(csv_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (row["name"], row["email"])
        )

conn.commit()


cursor.execute("SELECT name, email FROM users")
rows = cursor.fetchall()

print("Users stored in database:")
for row in rows:
    print(row)

conn.close()
