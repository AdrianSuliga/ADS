from zad1testy import runtests

# Adrian Suliga
# Program sprawdza dla każdego znaku w znaku s jaka jest długość palindromu o środku w rozważanym znaku, następnie
# zwraca największą długość jaka się pojawiła. Szacowana przeze mnie złożoność czasowa algorytmu to O(n^2), a pamięciow
# O(n) - program przechowuje dany napis o długości n

def ceasar( s ):
    n = len(s)
    max_cnt = -float('inf')
    for i in range(n):
        j, k = i - 1, i + 1
        cnt = 1
        while j > -1 and k < n and s[j] == s[k]:
            cnt += 2
            j -= 1
            k += 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
