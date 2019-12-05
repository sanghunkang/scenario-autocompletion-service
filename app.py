from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get_prediction')
def get_prediction():
    # terminate and response when one of action has reached

    return 'Hello, World!'

@app.route('/add_record')
def add_record():
    return 'Hello, World!'
