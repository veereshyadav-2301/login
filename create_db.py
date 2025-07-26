import sqlite3
import os

# Create the 'db' folder if it doesn't exist
if not os.path.exists('db'):
    os.makedirs('db')

# Connect to database
conn = sqlite3.connect('db/mydatabase.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

print("✅ Database and table created successfully!")
