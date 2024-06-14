from zad4ktesty import runtests
from math import inf

# Adrian Suliga
# Algorytm oblicza wartość funkcji f(i, j) takiej że:
# f(i, j) oznacza minimalny koszt dotarcia do pola (i, j)
# f(i, j) = min { f(i - 1, j), f(i, j - 1) } + T[i][j]
# f(0, 0) = 0
# Rozwiązaniem jest f(n - 1, n - 1)
# Złożoność czasową i pamięciową algorytmu szacuję na O(n^2)

def falisz(T):
    n = len(T)
    F = [[0 for _ in range(n)] for _ in range(n)]

    F[0][0] = 0
    for i in range(1, n):
        F[i][0] += F[i - 1][0] + T[i][0]
        F[0][i] += F[0][i - 1] + T[0][i] 

    for i in range(1, n):
        for j in range(1, n):
            F[i][j] = min(F[i - 1][j], F[i][j - 1]) + T[i][j]

    return F[n - 1][n - 1]

# Rekurencja ze słownikiem
"""def falisz ( T ):
    n = len(T)
    memo = {}

    return grid_travel(T, n - 1, n - 1, memo)

def grid_travel(T:list, i:int, j:int, memo:dict) -> int:
    if (i, j) in memo: return memo[(i, j)]
    if i == j == 0: return 0
    n = len(T)
    if -1 < i < n and -1 < j < n:
        res = min(grid_travel(T, i - 1, j, memo), grid_travel(T, i, j - 1, memo)) + T[i][j]
        memo[(i, j)] = res
        return res
    else:
        return inf"""

runtests ( falisz )
