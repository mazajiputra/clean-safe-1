import time
import board
import adafruit_shtc3
import pandas as pd
from datetime import datetime


#while True:
def baca_s(no_sensor):
    #time.sleep(5)
    i2c = board.I2C()   # uses board.SCL and board.SDA
    sht = adafruit_shtc3.SHTC3(i2c)
    temperature, relative_humidity = sht.measurements
    # print("Temperature: %0.1f C" % temperature)
    # print("Humidity: %0.1f %%" % relative_humidity)
    print(temperature)
    print(relative_humidity)
    print("")
    #Memasukkan data
    waktu=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    data = {
    'waktu': [waktu],
    's{no_sensor}_suhu': [temperature],
    's{no_sensor}_kelembaban': [relative_humidity],
}
    print(data)

    time.sleep(5)