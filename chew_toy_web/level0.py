from chew_toy_web import app
from flask import render_template

@app.route('/level0')
def level0():
    return render_template('message.html', message='Not here ...')
    
@app.route('/hidden_level0_flag')
def flag():
    return render_template('message.html', message='FIRST FLAG HERE')

