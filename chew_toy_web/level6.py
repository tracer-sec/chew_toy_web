from chew_toy_web import app, instance_id
from flask import render_template, request, session, redirect
import os
import sqlite3

def get_db():
    filename = 'level6_' + instance_id + '.db'
    creating = not os.path.isfile(filename)
    conn = sqlite3.connect(filename)
    if creating:
        print('creating db')
        c = conn.cursor()
        c.execute('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, public TEXT, private TEXT)')
        c.execute("INSERT INTO users ('username', 'password', 'public', 'private') VALUES ('admin', 'j6GM0bbCP8q9NQ1PotbZ1', 'i haz flag', 'FLAG_6_askdjaiwuelakwd')")
        c.execute("INSERT INTO users ('username', 'password', 'public', 'private') VALUES ('you', 'password', 'my password is password', 'TODO: stab gtrf')")
        conn.commit()
    return conn

@app.route('/level6', methods=['GET'])
def level6_get():
    if 'user_id' in session:
        return redirect('/level6/profile')
    return render_template('level6.html')

@app.route('/level6', methods=['POST'])
def level6_post():
    username = request.form['username']
    password = request.form['password']

    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT id, password FROM users WHERE username = ?', (username,))
    row = c.fetchone()
    if password == row[1]:
        session['level6_user_id'] = row[0]
    return redirect('/level6/profile')

@app.route('/level6/logout')
def level6_logout():
    del session['level6_user_id']
    return redirect('/level6')

@app.route('/level6/users', methods=['GET'])
def level6_users():
    users = []
    conn = get_db()
    c = conn.cursor()
    sql = 'SELECT id, username, public FROM users'
    for row in c.execute(sql):
        users.append({ 'id': row[0], 'username': row[1], 'public': row[2] })
    return render_template('level6_users.html', users=users)

@app.route('/level6/profile', methods=['GET'])
def level6_profile_get():
    if 'level6_user_id' not in session:
        return redirect('/level6')
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT id, username, password, public, private FROM users WHERE id = ?', (session['level6_user_id'],))
    row = c.fetchone()
    return render_template('level6_profile.html', user={ 'id': row[0], 'username': row[1], 'password': row[2], 'public': row[3], 'private': row[4] })

@app.route('/level6/profile', methods=['POST'])
def level6_profile_post():
    if 'level6_user_id' not in session:
        return redirect('/level6')
    id = request.form['id']
    public = request.form['public']
    private = request.form['private']
    conn = get_db()
    c = conn.cursor()
    c.execute('UPDATE users SET public=?, private=? WHERE id=?', (public, private, id,))
    conn.commit()
    return redirect('/level6/profile')

@app.route('/level6/password', methods=['POST'])
def level6_password_post():
    if 'level6_user_id' not in session:
        return redirect('/level6')
    id = request.form['id']
    password = request.form['password']
    conn = get_db()
    c = conn.cursor()
    c.execute('UPDATE users SET password=? WHERE id=?', (password, id,))
    conn.commit()
    return redirect('/level6/profile')

