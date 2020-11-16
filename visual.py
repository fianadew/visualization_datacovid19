import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


visual_covid = pd.read_csv('data_covid19.csv')

data_jakarta=visual_covid[visual_covid['key'] =='DKI JAKARTA'].copy()
data_jakarta['positif']=data_jakarta['positif'].astype(int)
data_jakarta['sembuh']=data_jakarta['sembuh'].astype(int)
data_jakarta['jumlah_kasus']=data_jakarta['jumlah_kasus'].astype(int)
data_jakarta['jumlah_sembuh']=data_jakarta['jumlah_sembuh'].astype(int)

print(data_jakarta['jumlah_kasus'])

'''
fig, ax=plt.subplots()
plt.plot(data_jakarta.index, data_jakarta.positif, c='black', marker='s')
plt.plot(data_jakarta.index, data_jakarta.sembuh,  c='maroon', marker='o')
plt.plot(data_jakarta.index, data_jakarta.meninggal, c='yellow', marker='o')
'''

g=sns.relplot(x='last_date', y='positif', data=data_jakarta, kind='line')

g.set_xticklabels(data_jakarta.last_date, rotation=20)

plt.grid()

plt.show()

'''
cov_jabar_tidy = (cov_jabar.drop(columns=[item for item in cov_jabar.columns
                                               if item.startswith('AKUMULASI') 
                                                  or 
item.startswith('DIRAWAT')])
                           .rename(columns=str.lower)
                           .rename(columns={'kasus': 'kasus_baru'})
                  )
cov_jabar_tidy['tanggal'] = pd.to_datetime(cov_jabar_tidy['tanggal']*1e6, unit='ns')
print('Lima data teratas:\n', cov_jabar_tidy.head())
'''

