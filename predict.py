import sys
import file
import train
import precision
import plot

def estimate_price(km, theta0, theta1):
    return theta0 + theta1 * km

def usage():
    print("Usage: " + sys.argv[0] + " [-b]")
    sys.exit(2)

if len(sys.argv) != 1 and (len(sys.argv) != 2 or sys.argv[1] != "-b"):
    usage()
bonus = True if len(sys.argv) == 2 else False
loop = True
while loop:
    try:
        km = float(input("km: "))
        loop = False
    except:
        print("km must be a number")
theta0, theta1 = file.read_theta()
data = file.read_data()
min_km = min(data, key = lambda t: t[0])[0]
max_km = max(data, key = lambda t: t[0])[0]
km = train.scale_km(km, min_km, max_km)
price = theta0 + (theta1 * km)
print ("estimated price: %.2f" % estimate_price(km, theta0, theta1))
if bonus:
    scaled_data = train.scale_data(data)
    p = precision.r_squared(scaled_data, theta0, theta1)
    print("precision: %.2f%%" % (p * 100))
    plot.draw(data, theta0, theta1)