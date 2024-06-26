from egzP5atesty import runtests 
from math import inf

# Adrian Suliga
# Algorytm oblicza dla każdego elementu gdzie znajduje się pierwszy element mniejszy od
# niego na lewo i prawo, następnie liczymy jaką maksymalną powierzchnię działek możemy kupić
# Szacuję złożoność czasową i pamięciową algorytmu na O(n).

def inwestor(T):
    n = len(T)
    Stack = [-1, 0]
    result = 0

    LS = [-1 for _ in range(n)]
    RS = [n for _ in range(n)]

    for i in range(1, n):
        while Stack[-1] != -1 and T[Stack[-1]] > T[i]:
            RS[Stack[-1]] = i
            Stack.pop()

        if T[i] == T[i - 1]:
            LS[i] = LS[i - 1]
        else:
            LS[i] = Stack[-1]

        Stack.append(i)

    for i in range(n):
        result = max(result, T[i] * (RS[i] - LS[i] - 1))

    return result

# Adrian Suliga, n^2
# Algorytm oblicza wartości funkcji f takiej że:
# f(i, j) - maks. powierzchnia zakupionych działek jeśli rozważamy działki od i. do j.
# f(i, j) = max { (j - i + 1) * min(F[i : j + 1], f(i + 1, j), f(i, j - 1)) }
# f(i, i) = T[i]
# Odpowiedzią do zadania jest wówczas max { f(i, j) | 0 <= i < n , 0 <= j < n }
# Przy czym aby optymalnie liczyć min(F[i : j + 1]), przed obliczaniem funkcji f musimy obliczyć
# wartości funkcji m:
# m(i, j) - powierzchnia zakupionych działek jeśli na pewno kupimy działki od i. do j.
# m(i, i) = T[i]
# m(i, j) = min { T[j], m(i, j - 1) }
# Szacuję złożoność czasową i pamięciową algorytmu na O(n^2)

"""def inwestor ( T ):
    n = len(T)
    F = [[-1 for _ in range(n)] for _ in range(n)] # tablica na wartości funkcji f
    M = [[inf for _ in range(n)] for _ in range(n)] # tablica na wartości funkcji m

    fill(M, T) # obliczamy m(i, j)

    for i in range(n): # base case
        F[i][i] = T[i]

    for i in range(1, n): # wartości funkcji f uzupełniamy wiersz po wierszu
        for j in range(n - i): # w danej chwili j odnosi się do początku rozważanego przedziału działek, a j + i do jego końca
            F[j][j + i] = max((i + 1) * M[j][j + i], F[j + 1][j + i], F[j][j + i - 1])

    result = -1
    for array in F: result = max(result, max(array))
    return result

def fill(M:list, T:list) -> None:
    n = len(T)

    for i in range(n): # base case
        M[i][i] = T[i]

    for i in range(n): # wzór rekurencyjny
        for j in range(i + 1, n):
            M[i][j] = min(T[j], M[i][j - 1])"""

runtests ( inwestor, all_tests=True )
