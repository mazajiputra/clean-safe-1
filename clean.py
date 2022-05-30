#Persiapan
from ref_r import setting_relay,r_off,r_on
import RPi.GPIO as GPIO
from time import sleep
from sensor_raw import waktu_now,baca_s
from cmultiplexer_raw import ganti_c
from datetime import datetime
from ref_data import simpan_dt
# from ref_0_utama import sen1,sen2,sen3,sen4
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


################################
def sen1(data):
    try:
        ganti_c(2)
        result=baca_s(1,data)
    except Exception as e:
        print('Error:',e)
    finally:
        return result
def sen2(data):
    try:
        ganti_c(4)
        result=baca_s(2,data)
    except Exception as e:
        print('Error:',e)
    finally:
        return result
def sen3(data):
    try:
        ganti_c(5)
        result=baca_s(3,data)
    except Exception as e:
        print('Error:',e)
    finally:
        return result
def sen4(data):
    try:
        ganti_c(7)
        result=baca_s(4,data)
    except Exception as e:
        print('Error:',e)
    finally:
        return result

##############
try:
    #r_off()#relay mati semua
    r_on()#relay nyala semua
    while (True):
        #Pencatatan waktu
        data_waktu = waktu_now()
        #Sementara, karena hanya sisa 1 sensor
        #1(channel 2, pin 12)
        data_full_1 = sen1(data_waktu)
        #1(channel 4, pin 16)
        data_full_2 = sen2(data_full_1)
        #3(channel 5, pin 20)
        data_full_3=sen3(data_full_2)
        # #4(channel 7, pin 21)
        data_full_4=sen4(data_full_3)
        ####
        #Simpan Data file file offline
        simpan_dt(data_full_4)
        ####
        #Istirahat
        sleep(15)#Istirahat 15 detik, pengukuran terhitung 20 detik, 
        #Jadi ada 5 detik untuk pengukuran keseleleruhan sensor
        print("===================================END+=====================================")
except KeyboardInterrupt:
    #r_off()#relay mati semua
    print("keluar")