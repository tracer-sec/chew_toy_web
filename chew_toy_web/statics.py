from chew_toy_web import app
from flask import render_template, send_from_directory, request

@app.route('/')
def index():
    return render_template('index.html', message='Hello world!')
    
@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
    
