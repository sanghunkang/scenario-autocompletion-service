# Scenario Autocompletion Service
This project is an microservice application to provide autocompletion of user scenario. For every action given by user, such as typing a key, the microservice predicts which action will be eventually given to the user. The project is also accompanied with a training environment.

# Dependencies
- python >= 3.8.0

```
flask >= 1.1.1
```

# Getting started
- (how to install)

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









APP
- Service Env

- Train Env
    - load data
    

    - push model