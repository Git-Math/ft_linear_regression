import sys
import file

learning_rate = 1
gradient_iter_nb = 100

def scale_km(km, min_km, max_km):
    return (km - min_km) / (max_km - min_km)

def scale_data(data):
    scaled_data = []
    min_km = min(data, key = lambda t: t[0])[0]
    max_km = max(data, key = lambda t: t[0])[0]
    for km, price in data:
        scaled_data.append((scale_km(km, min_km, max_km), price))
    return scaled_data

def gradient_descent_step(data, theta0, theta1, learning_rate):
    sum0 = 0.0
    sum1 = 0.0
    m = float(len(data))
    for km, price in data:
        price_diff = theta0 + (theta1 * km) - price
        sum0 += price_diff
        sum1 += price_diff * km
    theta0 -= learning_rate / m * sum0
    theta1 -= learning_rate / m * sum1
    return theta0, theta1    

data = file.read_data()
data = scale_data(data)
theta0, theta1 = file.read_theta()
for i in range(gradient_iter_nb):
    theta0, theta1 = gradient_descent_step(data, theta0, theta1, learning_rate)
file.write_theta(theta0, theta1)