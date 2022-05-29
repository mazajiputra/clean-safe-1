import pandas as pd
import os

def simpan_dt():
    #Menghapus file yg lama
    file = r'data\file_data.csv'
    if(os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)
        print("file deleted")
    else:
        print("file not found")