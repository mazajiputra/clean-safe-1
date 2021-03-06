import time
from tkinter.messagebox import RETRY
from unittest import result
from urllib import response
import board
import adafruit_shtc3
import pandas as pd
from datetime import datetime
import numpy as np 
from array import array
from struct import unpack
from copy import copy

from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection, \
    I2cDevice, SensirionI2cCommand, CrcCalculator
from ref_sensor_raw import Shtc3Temperature as Sht3xTemperature, Shtc3Humidity as Sht3xHumidity
# from sensirion_i2c_sht.sht3x import Sht3xTemperature, Sht3xHumidity

class Shtc3I2cCmdMeasure(SensirionI2cCommand):
    def __init__(self):
        super(Shtc3I2cCmdMeasure, self).__init__(
            command=0x7866,
            tx_data=[],
            rx_length=6,
            read_delay=0.02,
            timeout=0,
            crc=CrcCalculator(8, 0x31, 0xFF),
        )

    def interpret_response(self, data):
        checked_data = SensirionI2cCommand.interpret_response(self, data)
        temperature_ticks, humidity_ticks = unpack(">2H", checked_data)
        return Sht3xTemperature(temperature_ticks), Sht3xHumidity(humidity_ticks)

def cetak():
    with LinuxI2cTransceiver('/dev/i2c-1') as transceiver:
        device = I2cDevice(I2cConnection(transceiver), 0x70)
        response = device.execute(Shtc3I2cCmdMeasure())
        # print("Interval: {} ms".format(response.measure_interval_ms))
        # print("Temperature outside: {} °C".format(response.temperature_outside.degree_celsius))
        # print("Temperature inside: {}".format(response.temperature_inside))
        temperature,humidity=response
        return temperature,humidity


def waktu_now():
    waktu=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    d={'waktu':[waktu]}
    data_full=pd.DataFrame(data=d)
    print(data_full)
    #Membuat data frame
    return data_full


#while True:
def baca_s(no_sensor,data_lawas):
    try:
        result_a,result_b=cetak()
        temperature=result_a
        humidity=result_b
    except Exception as e:
        temperature=0
        humidity=0
        print('Error:',e)
    finally:
        #0 Siapkan DF
        data_balik = pd.DataFrame()
        #1. Konfirmasi data yg ada
        print(temperature)
        print(type(temperature))
        print(humidity)
        print("")
        #2. Data dibuat data frame
        d={f's{no_sensor}_suhu':[temperature],f's{no_sensor}_kelembaban':[humidity]}
        data_sensor=pd.DataFrame(data=d)
        # frames = [data_full, data_sensor]  # Or perform operations on the DFs
        data_balik = pd.concat([data_lawas, data_sensor], axis=1, join='outer')
        print("=============================================================================")
        return data_balik
        #Backup
        # data={f's{no_sensor}_suhu': temperature,f's{no_sensor}_kelembaban' : humidity}
        # data_full=Merge(data_full,data)