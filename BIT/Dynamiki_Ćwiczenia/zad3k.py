from zad3ktesty import runtests
from math import inf

# Adrian Suliga
# Rozważamy funkcję f(i) która oblicza minimalną ładną sumę przy założeniu, że
# do sumy należy i. liczba oraz rozważamy tylko liczby do i.

# f(i) = T[i] dla i < k
# f(i) = min { T[i] + f(j) | i - k <= j < i } dla i >= k

# Rozwiązaniem jest min { f(i) | len(T) - k <= i < len(T) }
# Algorytm oblicza wartości tej funkcji i zapisuje je do tablicy F[].
# Szacuję złożoność czasową algorytmu na O(nk), a pamięciową na O(n)

def ksuma(T, k):
    n = len(T)
    F = [T[i] for i in range(n)]

    for i in range(k, n):
        res = inf
        for j in range(i - k, i):
            res = min(res, F[j])
        F[i] += res
    
    return min(F[n - k : n])

# Rekurencja ze słownikiem
"""def ksuma( T, k ):
    res, n = inf, len(T)
    memo = {}

    for i in range(n - k, n):
        res = min(res, f(i, k, T, memo))

    return res

def f(i, k, T, memo):
    if i in memo: return memo[i]
    if i < k: return T[i]

    res = inf

    for j in range(i - k, i):
        res = min(res, f(j, k, T, memo) + T[i])

    memo[i] = res
    return res"""
    
runtests ( ksuma )