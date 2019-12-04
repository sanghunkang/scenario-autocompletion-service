# Scenario Autocompletion Service
This project is an microservice application to provide autocompletion of user scenario. That is, for every action given by user, the microservice predicts which will be the final action to be taken or required by the service. The project is also accompanied with a training environment.

# Dependencies
- python >= 3.8.0

# Getting started
- (how to install)

```
flask >= 1.1.1
```

## How it works?
### In the data collection time
- Whenever keyboard input is detected from the browser, the browser sends an HTTP request
- Sequence of keyboard input is recorded until the user reaches an end of some scenario

### In the training time
- Input: Sequence of keys + user profile, realtime hotscenario
- Output: The action finally taken at the end of scenario
- Model: Some variant of RNN + weighted sum of predictions from other models

### In the runtime
- Whenever keyboard input is detected from the browser, the browser sends an HTTP request
- The sequence detected thus far are input into the model and an action is predicted
- The service returns the action with highest confidence(?) as the response