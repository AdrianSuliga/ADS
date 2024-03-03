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
    i, j = 0, len(T) - 1
    while i < j:
        if T[j] - T[i] == x:
            return True
        elif T[j-1] - T[i] == x:
            return True
        elif T[j] - T[i+1] == x:
            return True
        j-=1
        i+=1
    return False

T = [randrange(1, 10) for _ in range(20)]
sortT(T)
print(searchT(T, 5))
print(T)