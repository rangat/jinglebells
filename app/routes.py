from app import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
    # Baseline intro screen
    return "Hello, World!"

@app.route('/santa/<int:santa_id>')
def santa(santa_id):
    # Get santa_id and find data to fill in app
    return str(santa_id)
