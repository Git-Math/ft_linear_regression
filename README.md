# Linear regression
[Linear regression](https://en.wikipedia.org/wiki/Linear_regression) implementation in order to predict the price of a car depending of its mileage.

- The Training part will train the model
- The Prediction part will make predictions using the trained model

## Training
Train the linear function with a [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) algorithm using the provided data.

### How to run
From the root of the repository run `python3 train.py [data file]`

### Example
```
$ python3 train.py data/data.csv

$ cat data/theta.csv
theta0,theta1
8008.3186216834365,-4656.271506734968
```

## Prediction
Asks for the mileage of a car and predicts its price using the [trained](#Training) model.

### How to run
From the root of the repository run `python3 predict.py [-b]`

### Option
-b: evaluate the precision of the predictions and display the linear function and data on a plot.

### Example
```
$ python3 predict.py -b
km: 50000
estimated price: 7427.07
precision: 73.30%
```

![linear_regression_plot](https://github.com/Git-Math/linear_regression/assets/11985913/cf1251e5-545b-45d6-9b8d-2bb65fa31db1)
