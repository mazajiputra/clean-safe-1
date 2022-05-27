#Persiapan
import RPi.GPIO as GPIO
from time import sleep
from jalan_raw import baca_s
import cmultiplexer_raw
from ref_relay import r_off
from ref_relay import r_on

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)
# Disable Warnings
GPIO.setwarnings(False)
# Set relay pins as output
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)


####################################################################################################
try:
    #r_off()#relay mati semua
    r_on()#relay nyala semua
    while (True):
        #Sementara, karena hanya sisa 1 sensor
        #1(channel 2, pin 12)
        ganti_c(2)
        baca_s()
        #1(channel 4, pin 16)
        ganti_c(2)
        baca_s()
        #3(channel 5, pin 20)
        ganti_c(2)
        baca_s()
        #4(channel 7, pin 21)
        ganti_c(2)
        baca_s()
except KeyboardInterrupt:
    #r_off()#relay mati semua
    print("keluar")