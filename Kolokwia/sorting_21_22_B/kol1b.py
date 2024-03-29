from kol1btesty import runtests

# Adrian Suliga
# Algorytm przepisuje każdy napis z wejściowej tablicy na 26 - elementową tablicę, gdzie każda komórka zlicza ile razy występuje
# każda litera w rozważanym napisie. Następnie używa algorytmu radix sort, aby posortować wyżej opisane tablice (zaczynamy od najmniej
# znaczącej litery). Następnie szuka najdłuższego podciągu jednakowych tablic. Długość znalezionego podciągu jest odpowiedzią do zadania.
# Złożoność czasową algorytmu szacuję na O(N)

def f(T):
    n = len(T)
    k = max_length(T)
    Letters = [[0 for _ in range(26)] for _ in range(n)] # O(n) na inicjalizację tablic
    count_letters(Letters, T)
    radix_sort(Letters, k)
    return longest_subsequence(Letters)

def count_letters(L, T):
    n = len(T)
    for i in range(n): # O(len(T[0]) + len(T[1]) + ...) = O(N) na zapisanie wystąpień do tablicy
        for j in range(len(T[i])):
            L[i][ord(T[i][j]) - ord('a')] += 1

def max_length(T):
    max_len = -float('inf')
    for i in range(len(T)): # O(n) na znalezienie najdłuższego napisu, oczywiści k < N, więc nie psuje nam to złożoności
        max_len = max(max_len, len(T[i]))
    return max_len

def longest_subsequence(L):
    max_len = -float('inf')
    i, j = 0, 0
    n = len(L)
    while j < n: # O(n) na znalezienie podciągu
        while j < n and are_the_same(L, i, j):
            j += 1
        max_len = max(max_len, j - i)
        i = j
    return max_len

def are_the_same(L, i, j): # O(1) na sprawdzenie czy dwie tablice są identyczne
    for k in range(26):
        if L[i][k] != L[j][k]: return False
    return True

def radix_sort(L, k):
    for i in range(25, -1, -1):
        counting_sort(L, i, k)

def counting_sort(L, ind, k): # O(n + k) na posortowanie po ind
    n = len(L)
    C = [0 for _ in range(k)]
    B = [0 for _ in range(n)]
    for i in range(n): C[L[i][ind]] += 1
    for i in range(1, k): C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        B[C[L[i][ind]] - 1] = L[i]
        C[L[i][ind]] -= 1
    for i in range(n): L[i] = B[i]

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )