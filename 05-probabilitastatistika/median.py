# Nama : Edwin
# NIM: D0221371
data = [0, 2, 2, 1, 3, 7, 1]

jumlah_data = len(data)
genap = jumlah_data % 2 == 0

for i in range(jumlah_data):
    for j in range(0, jumlah_data - i - 1):
        if data[j] > data[j + 1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp


print(f"Data setelah diurut: ", data)
if genap:
    index_satu = int(jumlah_data / 2)
    index_dua = int(jumlah_data / 2 + 1)

    median = (data[index_satu-1] + data[index_dua-1]) / 2
else:
    index_median = int(jumlah_data / 2)
    median = data[index_median]

print(f"Median: {median}")
