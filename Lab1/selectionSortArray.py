"""
Implement selection sort on array T
"""
from random import randrange
def sortT(T):
    n = len(T)
    for i in range(1, n):
        j = i - 1
        toInsert = T[i]
        while j > -1 and toInsert < T[j]:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = toInsert

T = [randrange(1, 100) for _ in range(10)]
sortT(T)
print(T)