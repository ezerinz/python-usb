data = [0, 2, 2, 1, 3, 7, 1]
frekuensi = {}

for i in data:
    if i in frekuensi:
        frekuensi[i] += 1
    else:
        frekuensi[i] = 1

maks = list(frekuensi.keys())[0]

for i in frekuensi:
    if frekuensi[maks] <= frekuensi[i]:
        maks = i

print("Modus:", maks)
