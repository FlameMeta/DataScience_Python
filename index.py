import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

data1 = pd.read_csv('data_csv/data1.csv')
# data2= pd.read_csv('data_csv/data2.csv')
data1.index = range(1, len(data1) + 1)



# Tampilkan 5 baris pertama
print(data1.dtypes)


print(data1.head())
print(data1.tail())
#dtype
print(data1.info())
#obejct
print(data1.nunique())

