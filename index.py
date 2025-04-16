import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv('data_csv/data1.csv')
# data2= pd.read_csv('data_csv/data2.csv')
data1.index = range(1, len(data1) + 1)


# gabungan = pd.concat([data1, data2], ignore_index=True)

# Tampilkan 5 baris pertama
print(data1.head())
print(data1.tail())
# data2.tail()
