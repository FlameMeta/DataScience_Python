import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv('data_csv/data1.csv')
data2= pd.read_csv('data_csv/data2.csv')


gabungan = pd.concat([data1, data2], ignore_index=True)

# Tampilkan 5 baris pertama
print(gabungan.head())
