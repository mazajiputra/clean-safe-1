import time
import board
import adafruit_shtc3
import pandas as pd
from datetime import datetime
import numpy as np 
def waktu_now():
    # global data_full
    # waktu=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # data={'waktu': [waktu]}
    # data_full=np.append(data_full, data)

    # print(data)
    # print(data_full)
#while True:
def baca_s(no_sensor):
    #global data_full
    try:
        #time.sleep(5)
        i2c = board.I2C()   # uses board.SCL and board.SDA
        sht = adafruit_shtc3.SHTC3(i2c)
        temperature, relative_humidity = sht.measurements
        # print("Temperature: %0.1f C" % temperature)
        # print("Humidity: %0.1f %%" % relative_humidity)
        print(temperature)
        print(relative_humidity)
        print("")      
        break
    except Exception:
        temperature=0
        relative_humidity=0

    #2_Perangkaian data
    data = {
    f's{no_sensor}_suhu': [temperature],
    f's{no_sensor}_kelembaban': [relative_humidity],
    }
    #3_Pengappen data ke data full

    # data_full=np.append(data_full, data)

    # print(data)
    # print(data_full)

    time.sleep(5)