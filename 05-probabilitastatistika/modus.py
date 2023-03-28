# Nama : Edwin
# NIM : D0221371
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

semua_sama = True
for j in frekuensi:
    if frekuensi[maks] != frekuensi[j]:
        semua_sama = False

# Menampilkan
print(f"Data: {data}")
print("Frekuensi: ")
for l in frekuensi:
    print(f"{l} = {frekuensi[l]}")

print()
if not semua_sama:
    print("Modus: ", end="")
    modus = []
    for k in frekuensi:
        if frekuensi[k] == frekuensi[maks]:
            modus.append(k)

    print(*modus, sep=", ")
else:
    print("Modus tidak ada")
