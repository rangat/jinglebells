from app import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
    # Baseline intro screen
    return "Hello, World!"

@app.route('/santa', methods=['GET'])
def santa():
    return request.data