def modus(data):
    frekuensi = {}
    for i in data:
        frek = 0
        for j in data:
            if i == j:
                frek += 1
                frekuensi[i] = frek

    maks = list(frekuensi.keys())[0]

    for i in frekuensi:
        if frekuensi[maks] < frekuensi[i]:
            maks = i

    semua_sama = True
    for j in frekuensi:
        if frekuensi[maks] != frekuensi[j]:
            semua_sama = False

    modus = []
    if not semua_sama:
        for k in frekuensi:
            if frekuensi[k] == frekuensi[maks]:
                modus.append(k)

    # Menampilkan
    print(f"Data: {data}")
    print("Frekuensi: ")
    for l in frekuensi:
        print(f"{l} = {frekuensi[l]}")

    if modus:
        print("Modus: ", end="")
        print(*modus, sep=", ")
    else:
        print("Modus tidak ada")


def median(data):
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


nim = [0, 2, 2, 1, 3, 7, 1]
modus(nim)
print("-"*15)
median(nim)
