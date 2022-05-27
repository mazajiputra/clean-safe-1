#Persiapan
import RPi.GPIO as GPIO
from time import sleep
from sensor_raw import baca_s
from cmultiplexer_raw import ganti_c

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)
# Disable Warnings
GPIO.setwarnings(False)
# Set relay pins as output
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

def r_off():
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)   
    sleep(2) 

def r_on():
    GPIO.output(12, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)   
    sleep(2)
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