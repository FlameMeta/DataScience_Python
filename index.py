import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data_csv/data1.csv')

# Data
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]
# a = [1, 2, 3, 4, 5]
# b = [2, 3, 5, 7, 11]

# # Membuat plot
# plt.plot(x, y)
# plt.plot(a, b)

# # Memberi label
# plt.title("Contoh Grafik Garis")
# plt.xlabel("Nilai x")
# plt.ylabel("Nilai y")

# # Menampilkan grafik
# plt.show()

plt.plot(data['kota'], data['percentase'])
plt.title('Grafik Penjualan')
plt.xlabel('Tanggal')
plt.ylabel('Penjualan')
plt.grid(True)
plt.show()
