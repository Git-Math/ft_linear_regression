import sys

def read_theta():
    try:
        with open("data/theta.csv", "r") as theta_file:
            theta_file.readline()
            theta_list = theta_file.readline().split(",")
            theta0 = float(theta_list[0])
            theta1 = float(theta_list[1])
            theta_file.close()
    except:
        theta0 = 0.0
        theta1 = 0.0
    return theta0, theta1

def write_theta(theta0, theta1):
    try:
        with open("data/theta.csv", "w") as theta_file:
            theta_file.write("theta0,theta1\n")
            theta_file.write(str(theta0) + "," + str(theta1) + "\n")
            theta_file.close()
    except:
        print("open theta file failed")
        exit(1)

def read_data():
    data = []
    try:
        with open("data/data.csv", "r") as data_file:
            data_file.readline()
            data_line = data_file.readline()
            while data_line:
                data_list = data_line.split(",")
                data.append((float(data_list[0]), float(data_list[1])))
                data_line = data_file.readline()
            data_file.close()
    except:
        print("data.csv invalid")
        exit(1)
    return data