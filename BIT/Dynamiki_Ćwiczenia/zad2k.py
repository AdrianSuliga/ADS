from zad2ktesty import runtests

# Adrian Suliga
# Algorytm szuka najdłuższego spójnego palindromu, najpierw szuka najdłuższego o nieparzystej ilości
# znaków, a potem o parzystej ilości. Robi to przechodząc po tablicy znaków, dla każdego znaku, jeśli
# znaki po jego lewej i prawej są takie same, to zwiększamy długość aktualnie znalezionego palindromu
# po czym porównujemy go z aktualnie najdłużyszm znalezionym. Szacuję złożoność czasową algorytmu na
# O(n^2), a pamięciową na O(1)

def palindrom( S ):
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

    return S[start : end + 1]

runtests ( palindrom )
