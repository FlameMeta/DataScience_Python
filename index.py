import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import numpy as np
import seaborn as sns

data1 = pd.read_csv('data_csv/data1.csv')
# data2= pd.read_csv('data_csv/data2.csv')
data1.index = range(1, len(data1) + 1)


dataobject = data1.select_dtypes(include=['object']).columns
datanumeric = data1.select_dtypes(include=np.number).columns.tolist()
# print("categorical variable")
# print(dataobject)
# print("\n \n")
# print("Numerical Variables: ")
# print(datanumeric)

# Tampilkan 5 baris pertama
# print(data1.dtypes)


# print(data1.head())
# print(data1.tail())
#dtype
# print(data1.info())
#obejct
# print(data1.nunique())

# print(data1.describe())



# visualisasi data numerik
for col in datanumeric:
    print(col)
    print('Skew: ', round(data1[col].skew(),2))
    plt.figure(figsize=(15,4))
    plt.subplot(1,2,1)
    data1[col].hist(grid=False)
    plt.ylabel('count')
    plt.subplot(1,2,2)
    sns.boxplot(x=data1[col])
    plt.show()

#visualisasi data numerik 2
    fig, axes = plt.subplots(3, 2, figsize=(18, 18))
fig.suptitle('Bar plot for all categorical variables in the dataset')

sns.countplot(ax=axes[0, 0], x='Fuel_Type', data=data1, color='blue',
              order=data1['Fuel_Type'].value_counts().index)
sns.countplot(ax=axes[0, 1], x='Transmission', data=data1, color='blue',
              order=data1['Transmission'].value_counts().index)
sns.countplot(ax=axes[1, 0], x='Owner_Type', data=data1, color='blue',
              order=data1['Owner_Type'].value_counts().index)
sns.countplot(ax=axes[1, 1], x='Location', data=data1, color='blue',
              order=data1['Location'].value_counts().index)
sns.countplot(ax=axes[2, 0], x='Brand', data=data1, color='blue',
              order=data1['Brand'].head(20).value_counts().index)
sns.countplot(ax=axes[2, 1], x='Model', data=data1, color='blue',
              order=data1['Model'].head(20).value_counts().index)

axes[1][1].tick_params(labelrotation=45)
axes[2][0].tick_params(labelrotation=90)
axes[2][1].tick_params(labelrotation=90)
