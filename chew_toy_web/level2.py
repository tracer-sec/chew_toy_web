from chew_toy_web import app
from flask import render_template, request, make_response
import base64
import json

@app.route('/level2')
def level2():
    cookie_base64 = request.cookies.get('data')
    cookie_json = base64.b64decode(cookie_base64).decode('utf-8') if cookie_base64 is not None else '{}'
    cookie_data = json.loads(cookie_json)
    if cookie_data.get('authed') == 'true':
        return render_template('message.html', message='THIRD_FLAG_HERE')
    else:
        cookie_data = { 'authed': 'false' }
        cookie_json = json.dumps(cookie_data)
        cookie_base64 = base64.b64encode(cookie_json.encode('utf-8'))
        response = make_response(render_template('message.html', message='Unauthorised!'))
        response.set_cookie('data', cookie_base64.decode('utf-8'), path='/level2')
        return response
        
