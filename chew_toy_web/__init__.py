from flask import Flask

app = Flask(__name__)

import chew_toy_web.statics
import chew_toy_web.level0
import chew_toy_web.level1
import chew_toy_web.level2
import chew_toy_web.level3
import chew_toy_web.level4

