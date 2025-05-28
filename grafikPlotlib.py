import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import numpy as np
import seaborn as sns

# Baca file CSV
data1 = pd.read_csv('data_csv/dataB/2022b.csv')

# Plot bar chart untuk Kelompok Umur 15-24
plt.figure(figsize=(12,6))
plt.bar(data1['Wilayah'], data1['Perokok 15-24'], color='skyblue')
plt.xticks(rotation=90)
plt.title('Persentase Penduduk Usia 15-24 per Kabupaten/Kota')
plt.xlabel('Kabupaten/Kota')
plt.ylabel('Persentase (%)')
plt.tight_layout()
plt.show()


# Set index ke 'Kabupaten/Kota' untuk mempermudah plot
data1.set_index('Kabupaten/Kota', inplace=True)

# Ambil hanya kolom-kolom usia
umur_cols = [col for col in data1.columns if 'Kelompok Umur' in col]

# Plot
data1[umur_cols].plot(kind='line', figsize=(14,7), marker='o')
plt.title('Persentase Penduduk Berdasarkan Kelompok Umur di Jawa Barat')
plt.xlabel('Kabupaten/Kota')
plt.ylabel('Persentase (%)')
plt.xticks(rotation=90)
plt.legend(title='Kelompok Umur')
plt.tight_layout()
plt.show()