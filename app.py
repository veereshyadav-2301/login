from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)  # ✅ THIS LINE CREATES THE FLASK APP

# Database connection function
def connect_db():
    return sqlite3.connect('db/mydatabase.db')


@app.route('/')
def home():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            return render_template('welcome.html', username=username)
        else:
            return "❌ Invalid username or password"

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
