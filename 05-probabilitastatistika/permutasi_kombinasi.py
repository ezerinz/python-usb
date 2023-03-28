def factorial(n):
    if n < 0:
        raise Exception(
            "Faktorial tidak berlaku untuk bilangan lebih kecil dari nol.")
    elif n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def permutasi(n, r):
    rumus = factorial(n) / factorial(n-r)
    return rumus


def kombinasi(n, r):
    rumus = factorial(n) / factorial(r) * factorial(n-r)
    return rumus


print(kombinasi(8, 3))
print(permutasi(3, 2))
print(factorial(5))
