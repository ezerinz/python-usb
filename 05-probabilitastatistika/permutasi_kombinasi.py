def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def factorial2(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


def permutasi(n, r):
    rumus = factorial(n) / factorial(n-r)
    return rumus


def kombinasi(n, r):
    rumus = factorial(n) / factorial(r) * factorial(n-r)
    return rumus


print(kombinasi(8, 3))
print(permutasi(3, 2))
print(factorial(3))
print(factorial2(3))
