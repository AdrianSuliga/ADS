"""
T - posortowana rosnąco tablica n elementów
znajdź najmniejszą liczbę całkowitą, której nie ma w tablicy
liczby w tablicy są z zakresu 0 ... m - 1
np. [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
n = 10
m = 12
"""
#Przechodzimy po elementach tablicy kolejno sprawdzając czy kolejny element ciągu jest równy indeksowi
#logarytmicznie: zaczynamy od środka i sprawdzamy czy indeksy się zgadzają
from random import randrange
def searchArray(T):
    for i in range(len(T)):
        if T[i] != i:
            return i
    return T[-1] + 1
def sortArray(T):
    n = len(T)
    for i in range(1, n):
        toInsert = T[i]
        j = i - 1
        while j > -1 and toInsert < T[j]:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = toInsert
T = [0, 1, 2, 3, 6, 7]
sortArray(T)
print(T)
print(searchArray(T))