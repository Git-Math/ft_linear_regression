import sys
import matplotlib
import matplotlib.pyplot as plt
import train

def draw(data, theta0, theta1):
    x_list = [x for x, y in data]
    y_list = [y for x, y in data]
    min_km = min(data, key = lambda t: t[0])[0]
    max_km = max(data, key = lambda t: t[0])[0]
    x0 = min_km
    y0 = theta0 + (theta1 * train.scale_km(x0, min_km, max_km))
    x1 = max_km
    y1 = theta0 + (theta1 * train.scale_km(x1, min_km, max_km))
    plt.scatter(x_list, y_list)
    plt.plot([x0, x1], [y0, y1])
    plt.xlabel("km")
    plt.ylabel("price")
    plt.show()