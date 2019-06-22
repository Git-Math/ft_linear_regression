import sys
import file

def estimate_price(km, theta0, theta1):
    return theta0 + theta1 * km

def usage():
    print("Usage: " + sys.argv[0] + " <km>")
    sys.exit(2)

def scale_km(km, min_km, max_km):
    return (km - min_km) / (max_km - min_km)

if len(sys.argv) != 2:
    usage()
try:
    km = float(sys.argv[1])
except:
    print("km must be a number")
    exit(2)
theta0, theta1 = file.read_theta()
data = file.read_data()
min_km = min(data, key = lambda t: t[0])[0]
max_km = max(data, key = lambda t: t[0])[0]
km = scale_km(km, min_km, max_km)
price = theta0 + (theta1 * km)
print (estimate_price(km, theta0, theta1))