x = [20, 40, 50, 30, 100, 70, 40, 60, 100]
y = [40, 100, 120, 80, 230, 180, 120, 140, 200]
n = len(x)


def sigma(x):
    hasil = 0
    for i in x:
        hasil += i

    return hasil


def kali(x, y):
    hasil = []
    for i in range(len(x)):
        nilai = x[i] * y[i]
        hasil.append(nilai)

    return hasil


def pangkatdua(x):
    hasil = []
    for i in range(len(x)):
        hasil.append(x[i] ** 2)
    return hasil


x2 = [i**2 for i in x]
sxx = sigma(pangkatdua(x)) - sigma(x) ** 2 / n
sxy = sigma(kali(x, y)) - (sigma(x) * sigma(y)) / n
syy = sigma(pangkatdua(y)) - sigma(y) ** 2 / n
akar_sxx = sxx**0.5
akar_syy = syy**0.5
r = sxy / (akar_sxx * akar_syy)
b1 = sxy / sxx
b2 = (sigma(y) - b1 * sigma(x)) / n
print(f"b1: {round(b1, 4)}")
print(f"b2: {round(b2, 4)}")
print(f"koefisien korelasi r: {round(r, 4)}")
print(f"Index Determinasi R: {round(r**2,4)}")
