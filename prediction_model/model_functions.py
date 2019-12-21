
class Predictor():
    def __init__(self, model_name):
        pass



    def predict_next_action(self):
                      
        end_signals = []                                # NOTE: 3.8 review candidate
        while (action not in end_signals):              # NOTE: 3.8 review candidate
            action = predict_next_action()
