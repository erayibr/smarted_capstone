def get_angle():

        f = open("../MPU92500/examples/basic-usage/magnetometer.txt", "r")
        angle = f.read()
        f.close()
        return angle