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

def sen1(data_full):
    try:
        ganti_c(2)
        baca_s(1,data_full)
    except Exception as e:
        print('Error:',e)
        sleep(3) 
def sen2(data_full):
    try:
        # ganti_c(4)
        ganti_c(4)
        baca_s(2,data_full)
    except Exception as e:
        print('Error:',e)
        sleep(3) 
def sen3(data_full):
    try:
        # ganti_c(5)
        ganti_c(5)
        baca_s(3,data_full)
    except Exception as e:
        print('Error:',e)
        sleep(3) 
def sen4(data_full):
    try:
        # ganti_c(7)
        ganti_c(7)
        baca_s(4,data_full)
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
        data_waktu=waktu_now()
        #Sementara, karena hanya sisa 1 sensor
        #1(channel 2, pin 12)
        data_full_1=sen1(data_waktu)
        #1(channel 4, pin 16)
        data_full_2=sen2(data_full_1)
        #3(channel 5, pin 20)
        data_full_3=sen3(data_full_2)
        #4(channel 7, pin 21)
        data_full_4=sen4(data_full_3)
        ####
        #Simpan Data file file offline
        # simpan_dt(data_full)
        ####
        #Istirahat
        sleep(15)
        print("===================================END+======================")
except KeyboardInterrupt:
    #r_off()#relay mati semua
    print("keluar")