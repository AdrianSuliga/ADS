"""
T - posortowana rosnąco tablica n elementów
znajdź najmniejszą liczbę całkowitą, której nie ma w tablicy
liczby w tablicy są z zakresu 0 ... m - 1 gdzie m > n
np. [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
n = 10
m = 12
"""
# Liniowo: przechodzimy po elementach tablicy kolejno sprawdzając czy kolejny element ciągu jest równy indeksowi
# Logarytmicznie: zaczynamy od środka i sprawdzamy czy indeksy się zgadzają
from random import randrange
import time
def searchArray(T): # O(n) - jedno przejście przez tablicę
    for i in range(len(T)):
        if T[i] != i:
            return i
    return T[-1] + 1

def searchArrayLog(T): # O(logn) - modyfikowane szukanie binarne
    def rec(T, ind, start, end, result):
        if start > end: return result
        if T[ind] == ind:
            start = ind + 1
        else:
            end = ind - 1
            result = ind
        return rec(T, (start+end)//2, start, end, result)
    n = len(T)
    return rec(T, n//2, 0, n - 1, -1)

def worseBinSearch(T, m): # O(m logn) - szukanie binarne dla każdego m, skoro m > n to jest to gorsze niż n * logn
    def find(T, x, start, end):
        if start > end:
            return False
        pivot = (start + end) // 2
        if x == T[pivot]: return True
        if x < T[pivot]:
            end = pivot - 1
        else:
            start = pivot + 1
        return find(T, x, start, end)
    n = len(T)   
    for i in range(m):
        if not find(T, i, 0, n - 1):
            return i

def sortArray(T):
    n = len(T)
    for i in range(1, n):
        toInsert = T[i]
        j = i - 1
        while j > -1 and toInsert < T[j]:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = toInsert

T = [0, 1, 2, 3, 6]
n = len(T)
start = time.time()
r = worseBinSearch(T, T[-1] + 1)
end = time.time()
print(r)
print(end - start)