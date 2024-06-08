from egz2btesty import runtests
from math import inf

# Adrian Suliga
# f(i, j) - optymalna suma odległości gdy rozważamy biurowce do i. włącznie oraz
# i. biurowiec ma j. działkę
# f(i, j) = abs(X[i] - Y[j]) + min { f(i - 1, k) | k < j }
# Algorytm oblicza wartości funkcji f(i, j) opisanej powyżej i zapisuje je do tablicy F[][]
# Na początku wypełniamy 0. wiersz wartościami |X[0] - Y[j]| gdzie 0 <= j < m
# następnie tablicę F zapełniamy przechodząc wierszu po wierszu wedle powyższego wzoru rekurencyjnego
# Złożoność czasową algorytmu oceniam na O(m^2 * n), a pamięciową na O(m * n)

def parking(X, Y):
    n, m = len(X), len(Y)
    F = [[inf for _ in range(m)] for _ in range(n)]

    for j in range(m): # zapełniamy pierwszy wiersz
        F[0][j] = abs(X[0] - Y[j])

    for i in range(1, n): # zapełniamy tablicę wiersz po wierszu
        min_prev = F[i - 1][0] # sprytnie zapamiętując poprzednią minimalną wartość f(i - 1, j - 1) 
        for j in range(1, m): # tak aby sprawnie policzyć min { f(i - 1, k) | k < j }
            min_prev = min(min_prev, F[i - 1][j - 1])
            if i > j: continue
            F[i][j] = abs(X[i] - Y[j]) + min_prev

    return min(F[n - 1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )