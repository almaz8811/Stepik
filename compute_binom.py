# Биномиальный коэффициент
from math import factorial


# объявление функции

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
