from chew_toy_web import app
from flask import render_template, request
import sqlite3

# ' OR 1=1;--

def get_db():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE data (key text, value text)')
    c.execute("INSERT INTO data VALUES ('foo', 'bar')")
    c.execute("INSERT INTO data VALUES ('domain', '2600.london')")
    c.execute("INSERT INTO data VALUES ('FOURTH_FLAG_HERE', 'flag')")
    c.execute("INSERT INTO data VALUES ('gtrf', 'stabbed')")
    conn.commit()
    return conn

@app.route('/level3', methods=['GET'])
def level3_get():
    return render_template('level3.html')
    
@app.route('/level3', methods=['POST'])
def level3_post():
    result = []
    conn = get_db();
    c = conn.cursor()
    sql = "SELECT * FROM data WHERE key = '" + request.form['key'] + "'"
    for row in c.execute(sql):
        result.append({ 'key': row[0], 'value': row[1] })
    return render_template('level3.html', result=result, sql=sql)
