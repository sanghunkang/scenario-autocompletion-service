from flask import Flask
from data_saver import save_data

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/predict')
def get_prediction():
    # terminate and response when one of action has reached
    action = predict_next_action()      # TODO: 3.8 review candidate
    end_signals = []
    while (action not in end_signals):           # TODO: 3.8 review candidate
        action = predict_next_action()

    # Pack something with action

    return "Some stringified json"

@app.route('/add_record')
def add_record():
    try:
        save_data()
        return "ok"
    except:
        return "internal server error"
        
