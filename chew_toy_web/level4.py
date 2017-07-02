from chew_toy_web import app
from flask import render_template, request
import sqlite3

# ' UNION SELECT name, sql FROM sqlite_master;--
# ' UNION SELECT here_it_is, '' FROM flag;--

def get_db():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE data (key text, value text)')
    c.execute("INSERT INTO data VALUES ('foo', 'bar')")
    c.execute("INSERT INTO data VALUES ('domain', '2600.london')")
    c.execute("INSERT INTO data VALUES ('gtrf', 'stabbed')")
    c.execute('CREATE TABLE oh_look_a_flag_table (here_it_is text)')
    c.execute("INSERT INTO oh_look_a_flag_table VALUES ('FIFTH_FLAG_HERE')")
    conn.commit()
    return conn

@app.route('/level4', methods=['GET'])
def level4_get():
    return render_template('level3.html')
    
@app.route('/level4', methods=['POST'])
def level4_post():
    result = []
    conn = get_db();
    c = conn.cursor()
    sql = "SELECT * FROM data WHERE key = '" + request.form['key'] + "'"
    for row in c.execute(sql):
        result.append({ 'key': row[0], 'value': row[1] })
    return render_template('level3.html', result=result, sql=sql)
