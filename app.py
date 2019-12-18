from flask import Flask
from flask_api import status

from data_saver import save_data
from model_functions import Predictor 
from data_management import DataManager

app = Flask(__name__)

# Load all data needed to provide service
predictor = Predictor(model_name=config["dataset_name"]) # TODO: Add env reader



# Routes
@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/api/predict")
def predict():
    try:
        # terminate and response when one of action has reached
        prediction, reasoning = predictor.predict_next_action()

        # Pack something with action

        # resp = make_response("Record not found", status.HTTP_400_BAD_REQUEST)
        # resp.headers["X-Something"] = "A value"
        return response
    except:
        response = make_response("INTERNAL SERVER ERROR", status.HTTP_500_INTERNAL_SERVER_ERROR)
        return response

@app.route("/api/add_record")
def add_record():
    try:
        save_data()
        return "ok"
    except:
        response = make_response("INTERNAL SERVER ERROR", status.HTTP_500_INTERNAL_SERVER_ERROR)
        return response
        
