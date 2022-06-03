import time
from tkinter.messagebox import RETRY
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
from sensirion_i2c_sht.sht3x import Sht3xTemperature, Sht3xHumidity

from struct import pack, unpack

class Sht3xTemperature():
    def __init__(self, rx_data):
        self.rx_data = rx_data

    @property
    def measure_interval_ms(self):
        return unpack(">H", self.rx_data[0:2])[0]

    @property
    def temperature_outside(self):
        return Sht3xTemperature(self.rx_data[2:4])

    @property
    def temperature_inside(self):
        return Sht3xTemperature(self.rx_data[4:6])

    # Optional: Provide conversion to string, e.g. for printing
    def __str__(self):
        return "{:.2f} ms interval, {:.2f} °C outside, {:.2f} °C inside".format(
            self.measure_interval_ms, self.temperature_outside,
            self.temperature_inside)

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
    # Provide conversion to integer (used in the command class)
   

    def interpret_response(self, data):
        checked_data = SensirionI2cCommand.interpret_response(self, data)
        # temperature_ticks, humidity_ticks = unpack(">2H", checked_data)
        temperature_ticks, humidity_ticks = unpack(">HH", checked_data)
        return Sht3xTemperature(temperature_ticks), Sht3xHumidity(humidity_ticks)
        # return temperature_ticks, humidity_ticks


def cetak():
    with LinuxI2cTransceiver('/dev/i2c-1') as transceiver:
        device = I2cDevice(I2cConnection(transceiver), 0x70)
        response = device.execute(Shtc3I2cCmdMeasure())
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
        temperature,humidity=cetak()
    except Exception as e:
        temperature=0
        humidity=0
        print('Error:',e)
    finally:
        #0 Siapkan DF
        data_balik = pd.DataFrame()
        #1. Konfirmasi data yg ada
        print(temperature)
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