import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import numpy as np

data1 = pd.read_csv('data_csv/data1.csv')
# data2= pd.read_csv('data_csv/data2.csv')
data1.index = range(1, len(data1) + 1)


dataobject = data1.select_dtypes(include=['object']).columns
datanumeric = data1.select_dtypes(include=np.number).columns.tolist()
print("categorical variable")
print(dataobject)
print("\n \n")
print("Numerical Variables: ")
print(datanumeric)

# Tampilkan 5 baris pertama
# print(data1.dtypes)


# print(data1.head())
# print(data1.tail())
#dtype
# print(data1.info())
#obejct
# print(data1.nunique())

# print(data1.describe())

