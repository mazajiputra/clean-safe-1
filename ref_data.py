import pandas as pd
import os


def simpan_dt(df_baru):
    #Mengecek file yg lama
    file = 'data/file_data.csv'
    if(os.path.exists(file) and os.path.isfile(file)):
        # os.remove(file)
        # print("file deleted")
        #Bila file nya ada tambah
        df_lama=pd.read_csv('data/file_data.csv')
        df_mix=pd.concat([df_lama, df_baru],ignore_index=True)
        print(df_mix)

        #Masukkan ke file lagi
        df_mix.to_csv('data/file_data.csv', index=True)

    else:
        print("file not found, make again")

        df_baru.to_csv('data/file_data.csv', index=True)

    # #create DataFrame
    # df0 = pd.DataFrame({'waktu': [0],
    #                 's1_suhu': [0],
    #                 's1_kelembaban': [0],
    #                 's2_suhu': [0],
    #                 's2_kelembaban': [0],
    #                 's3_suhu': [0],
    #                 's3_kelembaban': [0],
    #                 's4_suhu': [0],
    #                 's4_kelembaban': [0],
    #                 })









    #view DataFrame


    # print (df0)

    #export DataFrame to CSV file
    df0.to_csv('data/file_data.csv', index=True)



    #Gabungkan kedua data frame
    df_mix=pd.concat([df_lama, df_baru],ignore_index=True)

    df0.to_csv('data/file_data.csv', index=True)


    df_check=pd.read_csv('data/file_data.csv')
    print(df_check.head())
