from unittest import result
import pandas as pd
import os


def simpan_dt(df_baru):
    #Mengecek file yg lama
    file = 'data/file_data.csv'
    if(os.path.exists(file) and os.path.isfile(file)):
        # os.remove(file)
        # print("file deleted")
        #Bila file nya ada, tambah data
        #1. data di file dibaca
        df_lama=pd.read_csv('data/file_data.csv')
        #2. data dari file + data baru dimix
        df_mix=pd.concat([df_lama, df_baru],ignore_index=True,sort=False)
        print(df_mix.tail())
        #3 data lengkap sudah siap, Masukkan ke file lagi
        df_mix.to_csv('data/file_data.csv', index=False)
        print("File berhasil diperbarui")

    else:
        #export DataFrame to CSV file
        df_baru.to_csv('data/file_data.csv', index=False, header=True)
        print(df_baru)
        print("file not found, make again2")
        