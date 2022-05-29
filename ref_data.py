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

#create DataFrame
df0 = pd.DataFrame({'waktu': [0],
                   's1_suhu': [0],
                   's1_kelembaban': [0],
                   's2_suhu': [0],
                   's2_kelembaban': [0],
                   's3_suhu': [0],
                   's3_kelembaban': [0],
                   's4_suhu': [0],
                   's4_kelembaban': [0],
                   })

#view DataFrame
print (df0)