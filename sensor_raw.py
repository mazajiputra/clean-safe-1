import time
import board
import adafruit_shtc3
import pandas as pd
from datetime import datetime
import numpy as np 
from array import array
def waktu_now():
    global data_full
    data_full=[]
    waktu=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data={'waktu': [waktu]}
    data_full=np.concatenate(data_full, data,axis=0)

    print(data)
    print(data_full)
#while True:
def baca_s(no_sensor):
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
    
    except Exception:
        temperature=0
        relative_humidity=0
    finally:
        #2_Perangkaian data
        global data_full
        data = {
            f's{no_sensor}_suhu': [temperature],
            f's{no_sensor}_kelembaban': [relative_humidity],
        }
        #3_Pengappen data ke data full

        data_full=np.concatenate(data_full, data,axis=0)

        print(data)
        print(data_full)
        

        time.sleep(5)