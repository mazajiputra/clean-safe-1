#Persiapan
from ref_r import setting_relay,r_off,r_on
import RPi.GPIO as GPIO
from time import sleep
from sensor_raw import waktu_now,baca_s
from cmultiplexer_raw import ganti_c
from datetime import datetime
from ref_data import simpan_dt
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
        # ganti_c(4)
        ganti_c(2)
        baca_s(2)
    except Exception as e:
        print('Error:',e)
        sleep(3) 
def sen3():
    try:
        # ganti_c(5)
        ganti_c(2)
        baca_s(3)
    except Exception as e:
        print('Error:',e)
        sleep(3) 
def sen4():
    try:
        # ganti_c(7)
        ganti_c(2)
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
        #Pencatatan waktu
        waktu_now()
        #Sementara, karena hanya sisa 1 sensor
        #1(channel 2, pin 12)
        sen1()
        #1(channel 4, pin 16)
        sen2()
        #3(channel 5, pin 20)
        sen3()
        #4(channel 7, pin 21)
        sen4()
        ####
        #Simpan Data file file offline
        simpan_dt()
        ####
        #Istirahat
        sleep(15)
        print("===================================END+======================")
except KeyboardInterrupt:
    #r_off()#relay mati semua
    print("keluar")