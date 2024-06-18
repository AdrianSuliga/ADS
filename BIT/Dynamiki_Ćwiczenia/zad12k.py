from zad12ktesty import runtests 
from math import inf

# f(i, j) - najkrótszy czas remontu jeśli rozważamy gminy od 0 do i włącznie i mamy do rozdysponowania j firm
# f(i, k) = min { max { f(j, k - 1), s(j + 1, i) } | 0 <= j < i } gdzie s(j + 1, i) to suma liczb od T[j + 1] do T[i] włącznie
# Rozwiązaniem zadania jest wówczas f(n - 1, k)
# f(i, 1) = s(0, i)
# f(0, j) = T[0]
# Żeby efektywnie obliczyć s(i, j), to przed liczeniem f algorytm oblcza wartości
# funkcji s(i, j) i zapisuje je do tablicy n x n.
# Szacuję złożoność czasową algorytmu na O(n^2 * k), a pamięciową na O(nk + n^2)

def autostrada(T, k):
    n = len(T) # poniższe tablice są źródłem złożoności pamięciowe O(nk + n^2)
    F = [[inf for _ in range(k)] for _ in range(n)] # O(nk)
    S = [[-1 for _ in range(n)] for _ in range(n)] # O(n^2)

    fill(S, T) # oblicz wartości s(i, j)

    for i in range(n): # warunki brzegowe
        F[i][0] = S[0][i]
    for j in range(k):
        F[0][j] = T[0]

    for i in range(1, n):
        for j in range(1, k):
            result = inf
            for l in range(i):
                result = min(result, max(F[l][j - 1], S[l + 1][i]))
            F[i][j] = result

    return F[n - 1][k - 1] 

def fill(S, T):
    n = len(T)

    for i in range(n):
        S[i][i] = T[i]

    for i in range(n):
        for j in range(i + 1, n):
            S[i][j] = S[i][j - 1] + T[j]

# Rekurencja ze spamiętywaniem 
"""def autostrada( T, k ):
    n = len(T)

    F = [[inf for _ in range(k)] for _ in range(n)]

    return f(n - 1, k, T, F)

def f(i, k, T, F):
    if F[i][k - 1] != inf: return F[i][k - 1]
    if k == 1: return s(0, i, T)
    if i == 0: return T[0]

    result = inf

    for j in range(i):
        result = min(result, max(f(j, k - 1, T, F), s(j + 1, i, T)))
    
    F[i][k - 1] = result
    return result"""

def s(i, j, T):
    sum = 0
    for k in range(i, j + 1):
        sum += T[k]
    return sum

runtests ( autostrada,all_tests=True )
