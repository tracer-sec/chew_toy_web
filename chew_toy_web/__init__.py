from flask import Flask

app = Flask(__name__)
app.secret_key = '4`$<s/=*)qe@jq%L4:.^U:BX6_5X-&kK'
app.config['SESSION_COOKIE_HTTPONLY'] = False

instance_id = '5000'

import chew_toy_web.statics
import chew_toy_web.level0
import chew_toy_web.level1
import chew_toy_web.level2
import chew_toy_web.level3
import chew_toy_web.level4
import chew_toy_web.level5
import chew_toy_web.level6
