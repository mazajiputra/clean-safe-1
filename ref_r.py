import RPi.GPIO as GPIO
from time import sleep
def setting_relay():
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