from gps import gps 
from time import sleep

if __name__ == '__main__':
    print('starting gps')
    gps.gps_init('192.168.1.2','55556')
    print('reading data')
    while True:
        print(gps.get_latitude())
        print(gps.get_longitude())
        sleep(.5)
