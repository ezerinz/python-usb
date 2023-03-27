import math

angka = [50, 53, 64, 73,
         75, 76, 58, 67,
         74, 74, 73, 72,
         72, 73, 73, 72,
         79, 71, 70, 75,
         78, 52, 64, 74,
         75, 74, 72, 74,
         75, 74, 72, 68,
         79, 71, 79, 69,
         71, 70, 70, 79]
"""
angka = [68, 84, 75, 82, 68, 90, 62, 88, 76, 93,
         73, 79, 88, 73, 60, 93, 71, 59, 85, 75,
         61, 65, 75, 87, 74, 62, 95, 78, 63, 72,
         66, 78, 82, 75, 94, 77, 69, 74, 68, 60,
         96, 78, 89, 61, 75, 95, 60, 79, 83, 71,
         79, 62, 67, 97, 78, 85, 76, 65, 71, 75,
         65, 80, 73, 57, 88, 78, 62, 76, 53, 74,
         86, 67, 73, 81, 72, 63, 76, 75, 85, 77]
"""


def jumlah_kelas(n):
    k = 1 + 3.32 * math.log10(n)
    return round(k)


def hitung_interval(maks, min, kelas):
    interval = (maks - min) / kelas
    return round(interval)


def kategori(maks, min, interval):
    lst = []
    for i in range(min, maks, interval):
        lst.append(i)

    jarak = []
    nambah = False

    for i in lst:
        data = [i, i+(interval-1)]
        if lst[-1]+(interval-1) != maks and i == lst[-2]:
            data = [i, maks]
            nambah = True
        jarak.append(data)
    if nambah:
        jarak.pop()
    return jarak


def hitung_frekuensi(maks, min, interval, data):
    frekuensi = {}
    kelas_data = kategori(maks, min, interval)

    for k in range(len(kelas_data)):
        key = f"{kelas_data[k][0]} - {kelas_data[k][1]}"
        frekuensi[key] = 0
        for l in data:
            if kelas_data[k][0] <= l <= kelas_data[k][1]:
                frekuensi[key] += 1

    return frekuensi


def midpoint(kategori):
    mid = {}

    for k in range(len(kategori)):
        key = f"{kategori[k][0]} - {kategori[k][1]}"
        mid[key] = (kategori[k][0] + kategori[k][1]) / 2

    return mid


def mean_kelompok(mid, freq, data, jumlah_data):
    total = 0
    for z in range(len(data)):
        key = f"{data[z][0]} - {data[z][1]}"
        total += mid[key] * freq[key]
    hasil = total / jumlah_data
    return round(hasil, 2)


def mean_tunggal(data):
    hasil = sum(data) / len(data)
    return hasil


terbesar = max(angka)
terkecil = min(angka)
jumlah_data = len(angka)
jumlah_kelas = jumlah_kelas(jumlah_data)
interval = hitung_interval(terbesar, terkecil, jumlah_kelas)
frekuensi = hitung_frekuensi(terbesar, terkecil, interval, angka)
print(f"Jumlah Data: {jumlah_data}")
print(f"Nilai Terkecil: {terkecil}")
print(f"Nilai Terbesar: {terbesar}")
print(f"Jumlah Kelas: {jumlah_kelas}")
print(f"Interval: {interval}")
print("Distribusi Frekuensi")
for i in frekuensi:
    print(f"{i} = {frekuensi[i]}")

print()
kategori = kategori(terbesar, terkecil, interval)
midpoint = midpoint(kategori)
for i in midpoint:
    print(f"{i} = {midpoint[i]}")
mean = mean_kelompok(midpoint, frekuensi, kategori, jumlah_data)
print(f"Mean = {mean}")
