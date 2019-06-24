import sys

def calc_mean_price(data):
    mean = 0
    for km, price in data:
        mean += price
    mean /= len(data)
    return mean

def r_squared(data, theta0, theta1):
    sum0 = 0
    sum1 = 0
    mean_price = calc_mean_price(data)
    for km, price in data:
        predicted_price = theta0 + (theta1 * km)
        sum0 += (price - predicted_price) ** 2
        sum1 += (price - mean_price) ** 2
    return 1 - (sum0 / sum1)