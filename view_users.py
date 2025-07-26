import sqlite3

# Connect to your database
conn = sqlite3.connect('db/users.db')
cursor = conn.cursor()

# Select all users
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

# Print the result
print("\n--- Registered Users ---")
for user in users:
    print(f"ID: {user[0]}, Username: {user[1]}, Password: {user[2]}")

conn.close()
