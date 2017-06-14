from chew_toy_web import app
from flask import render_template, request, make_response

@app.route('/level1')
def level1():
    if request.cookies.get('authed') == 'true':
        return render_template('index.html', message='SECOND_FLAG_HERE')
    else:
        response = make_response(render_template('index.html', message='Unauthorised!'))
        response.set_cookie('authed', 'false', path='/level1')
        return response
        
