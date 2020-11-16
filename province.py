import requests
import pandas as pd
from pandas import ExcelWriter
from openpyxl.workbook import Workbook
import matplotlib.pyplot as plt
from datetime import datetime

#Mengambil data yang berasal dari APIs yang telah disediakan
url = 'https://data.covid19.go.id/public/api/prov.json'
r = requests.get(url)
data = r.json()

#Mengubah data JSON menjadi Data Frame
df=pd.DataFrame(data)
time=df['last_date']

#List dan Data Frame kosong untuk diisi
data_valid=[]
real_data=[]
lokasi_data=[]
kasus = pd.DataFrame()


#Unpack data untuk mendapatkan data kasus
for k in (df['list_data'].keys()):
    data_valid.append(df['list_data'][k])
covid = pd.DataFrame(data_valid)
kasus =covid[['jumlah_kasus', 'jumlah_sembuh', 'jumlah_meninggal', 'jumlah_dirawat']]

#Unpack data untuk mendapatkan data penambahan
for i in covid['penambahan'].keys():
    real_data.append((covid['penambahan'][i]))

#Unpack data untuk mendapatkan data lokasi
for j in covid['lokasi'].keys():
    lokasi_data.append(covid['lokasi'][j])

#Mengubah tiap list menjadi Data Frame
lokasi = pd.DataFrame(lokasi_data)
real = pd.DataFrame(real_data)

#Marging data yang didapat menjadi satu kolom
df_col=pd.concat([time, real, lokasi, kasus], axis=1)
df_col.index = covid['key']

with open("data_covid19.csv","a") as f:
    df_col.to_csv(f,header=False,index=True)


fig, ax = plt.subplots()
ax.plot (df_col.index[:5], df_col.positif[:5], c='black', label='Positif', linestyle='--', marker='o')
ax.plot(df_col.index[:5], df_col.sembuh[:5], c='maroon', label='Sembuh', marker='s')
ax.plot(df_col.index[:5], df_col.meninggal[:5], c='blue', label='Meninggal', marker='o')
ax.set_xticklabels(df_col.index, rotation=10)

plt.title('DATA COVID INDONESIA')
plt.legend()
plt.grid()
plt.show()
fig.savefig('covid.png', dpi=300)

'''
fig, ax = plt.subplots()
ax.bar(df_col.index, df_col['positif'], label='Positif')
ax.set_xticklabels(df_col.index, rotation=90)
ax.set_ylabel('Jumlah Manusia')
ax.legend()
plt.show()
'''''

'''
Background Erase is important to make your photo more powerful.

SERVICE :
- Background erase service
- Making logo service
- Edit photo service
- collage photo service
- Add another background service
- Manipulation photo
- Resize photo

I can work fast if you want.
'''