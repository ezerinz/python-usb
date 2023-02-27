data = [54, 55, 50, 54]
jumlah_data = len(data)
total = 0

for i in range(jumlah_data):
    total += data[i]

mean = total / jumlah_data
print(f"Mean: {mean}")
