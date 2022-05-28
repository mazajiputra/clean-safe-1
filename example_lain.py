import busio
import time
import board
import adafruit_shtc3

i2c = busio.I2C(board.SCL, board.SDA)
sht = adafruit_shtc3.SHTC3(i2c)
while True:
    print(sht.temperature)
    time.sleep(1)