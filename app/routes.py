from app import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
    # Baseline intro screen
    return "Hello, World!"

@app.route('/santa/<int:santa_id>', methods=['GET'])
def santa(santa_id):
    # Get santa_id and find data to fill in app
    new_user = request.args.get('new_user')
    if  new_user and new_user.isdigit() and int(new_user)==1:
        # This link adds new users to santa_id
        return "New User"
    return str(santa_id)
