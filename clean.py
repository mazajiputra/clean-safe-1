#Persiapan
from ref_r import setting_relay,r_off,r_on
import RPi.GPIO as GPIO
from time import sleep
from sensor_raw import waktu_now,baca_s
from cmultiplexer_raw import ganti_c
from datetime import datetime
# Mengatur data
import pandas as pd

##########################################################
#=========Setting=============
setting_relay()

####################################################################################################
#def waktu_now():#Untuk imput data waktu
 #   try:
        
   # except Exception as e:
  #  print('Error:',e)

def sen1():
    try:
        ganti_c(2)
        baca_s(1)
    except Exception as e:
        print('Error:',e)
        sleep(3) 
def sen2():
    try:
        ganti_c(4)
        baca_s(2)
    except Exception as e:
        print('Error:',e)
        sleep(3) 
def sen3():
    try:
        ganti_c(5)
        baca_s(3)
    except Exception as e:
        print('Error:',e)
        sleep(3) 
def sen4():
    try:
        ganti_c(7)
        baca_s(4)
    except Exception as e:
        print('Error:',e)
        sleep(3) 
################################


##############
try:
    #r_off()#relay mati semua
    r_on()#relay nyala semua
    while (True):
        data_full=0
        #Pencatatan waktu
        waktu_now()
        #Sementara, karena hanya sisa 1 sensor
        #1(channel 2, pin 12)
        sen1()
        #1(channel 4, pin 16)
        sen1()
        #3(channel 5, pin 20)
        sen1()
        #4(channel 7, pin 21)
        sen1()
        #Istirahat
        sleep(30)
except KeyboardInterrupt:
    #r_off()#relay mati semua
    print("keluar")