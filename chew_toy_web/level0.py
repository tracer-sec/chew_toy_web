from chew_toy_web import app
from flask import render_template

@app.route('/level0')
def level0():
    return render_template('index.html', message='FIRST_FLAG_HERE')
    
