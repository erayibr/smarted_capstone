# MPU6050 9-DoF Example Printout

from mpu9250_i2c import *
import numpy as np

def get_angle():
    # time.sleep(1) # delay necessary to allow mpu9250 to settle

    # while 1:
    #     try:
            # ax,ay,az,wx,wy,wz = mpu6050_conv() # read and convert mpu6050 data
    mx,my,mz = AK8963_conv() # read and convert AK8963 magnetometer data
    # except:
    #     continue
    
    # print('{}'.format('-'*30))
    # print('accel [g]: x = {0:2.2f}, y = {1:2.2f}, z {2:2.2f}= '.format(ax,ay,az))
    # print('gyro [dps]:  x = {0:2.2f}, y = {1:2.2f}, z = {2:2.2f}'.format(wx,wy,wz))
    # print('mag [uT]:   x = {0:2.2f}, y = {1:2.2f}, z = {2:2.2f}'.format(mx,my,mz))
    # print("angle data: " + str((np.arctan2(my,mx))*180/np.pi))
    # print('{}'.format('-'*30))
    
    return np.arctan2(my,mx)*180/np.pi