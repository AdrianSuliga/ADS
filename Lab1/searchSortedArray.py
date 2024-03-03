"""
Czy istnieją i,j w posortowanej rosnąco tablicy takie że T[j] - T[i] == x 
"""
#Przesuwać wskaźniki od końców (liniowe)
from random import randrange
def sortT(T):
    n = len(T)
    for i in range(1, n):
        toInsert = T[i]
        j = i - 1
        while j > -1 and T[j] > toInsert:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = toInsert
def searchT(T, x):
    n = len(T)
    for i in range(n - 1, -1, -1):
        j = 0
        while T[i] - T[j] > x:
            j += 1
        if T[i] - T[j] == x: return True
    return False

T = [262, 300, 310, 315, 317, 3200]
sortT(T)
print(searchT(T, 17))
print(T)