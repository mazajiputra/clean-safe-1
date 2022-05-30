import pandas as pd
import os


def simpan_dt(data):
    #Menghapus file yg lama
    # file = 'data/file_data.csv'
    # if(os.path.exists(file) and os.path.isfile(file)):
    #     os.remove(file)
    #     print("file deleted")
    # else:
    #     print("file not found")

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

    #export DataFrame to CSV file
    df0.to_csv('data/file_data.csv', index=True)

    #Siapkaan data baru
    df_baru=pd.DataFrame(data)
    print("")
    print(df_baru)

    with open('data/file_data.csv', 'a') as f:
        df_baru.to_csv(f, header=f.tell()==0)
    # print message
    print("Data appended successfully.")

    df_check=pd.read_csv('data/file_data.csv')
    print(df_check.head())
