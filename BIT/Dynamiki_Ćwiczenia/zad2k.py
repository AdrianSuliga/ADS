from zad2ktesty import runtests

# Adrian Suliga
# Algorytm oblicza następującę funkcję zapisując jej wyniki do tablicy F[][]
# f(i, j) - odpowiada na pytanie czy napis zaczynający się w i a kończący na j jest palindromem
# f(i, j) = False gdy S[i] != S[j]
# f(i, j) = f(i + 1, j - 1) gdzie j - i > 1
# f(i, i) = True
# f(i - 1, i) = True gdy S[i - 1] == S[i]
# Szacuję złożoność czasową algorytmu na O(n^2), a pamięciową na O(n^2)

def palindrom(S):
    n = len(S)
    F = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n): # pojedyncze znaki to palindromy
        F[i][i] = True

    for i in range(1, n): # napisy o 2 jednakowych znakach to palindromy
        if S[i - 1] == S[i]: F[i - 1][i] = True
        else: F[i - 1][i] = False

    for i in range(2, n): # pętlę uzupełniają tablicę skos po skosie
        for j in range(n - i): # w danym wykonaniu 2 pętli jesteśmy w wierszu j i kolumnie j + i
            if S[j] == S[j + i]:
                F[j][j + i] = F[j + 1][j + i - 1]
            else:
                F[j][j + i] = False

    start, end, cnt = 0, n - 1, 0

    for i in range(n):
        for j in range(i + 1, n):
            if F[i][j] and j - i + 1 > cnt: # jeśli jest palindromem i jest dłuższy niż najdłuższy dotychczas znaleziony
                cnt = j - i + 1
                start, end = i, j

    return S[start : end + 1]

# Adrian Suliga
# Algorytm szuka najdłuższego spójnego palindromu, najpierw szuka najdłuższego o nieparzystej ilości
# znaków, a potem o parzystej ilości. Robi to przechodząc po tablicy znaków, dla każdego znaku, jeśli
# znaki po jego lewej i prawej są takie same, to zwiększamy długość aktualnie znalezionego palindromu
# po czym porównujemy go z aktualnie najdłużyszm znalezionym. Szacuję złożoność czasową algorytmu na
# O(n^2), a pamięciową na O(1)

"""def palindrom( S ):
    n = len(S)
    result = -1
    start, end = -1, -1
    for i in range(n):
        j, k = i - 1, i + 1
        cnt = 1
        while j > -1 and k < n and S[j] == S[k]:
            cnt += 2
            j -= 1
            k += 1
        
        if cnt > result:
            result = cnt
            start, end = j + 1, k - 1

    for i in range(n - 1):
        j, k = i - 1, i + 2
        if S[i] == S[i + 1]:
            cnt = 2
            while j > -1 and k < n and S[j] == S[k]:
                cnt += 2
                j -= 1
                k += 1
            
            if cnt > result:
                result = cnt
                start, end = j + 1, k - 1

    return S[start : end + 1]"""

runtests ( palindrom )
#print(palindrom("aacacca"))