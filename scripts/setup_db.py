import sqlite3

conn = sqlite3.connect('documents.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    upload_date TEXT,
    content TEXT
)
''')

conn.commit()
conn.close()

print("Database and successfully created!")