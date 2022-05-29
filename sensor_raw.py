import time
from tkinter.messagebox import RETRY
import board
import adafruit_shtc3
import pandas as pd
from datetime import datetime
import numpy as np 
from array import array
def waktu_now(data_full):
    waktu=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data_full={'waktu': waktu}
    print(data_full)
    return data_full
#while True:
def baca_s(no_sensor,data_full):
    print(data_full)
    try:
        time.sleep(5)
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
        key='s'+str(no_sensor)+'suhu'
        data_full[key] = temperature
        # data_full.update({f's{no_sensor}_suhu'= temperature})

        # data_full[f's{no_sensor}_suhu']= temperature
        # data_full[f's{no_sensor}_kelembaban'] = relative_humidity
        # print(data_suhu,data_kelembaban)
        print(data_full)
        return data_full