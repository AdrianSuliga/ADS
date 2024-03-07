"""
implement merge sort on array
"""
from random import randrange
import time
def mergeSortClean(T):
    pass
def mergeSortWithPythonTricks(T):
    n = len(T)
    if n == 1:
        return
    
    pivot = n//2
    L = T[:pivot]
    R = T[pivot:]

    mergeSortWithPythonTricks(L)
    mergeSortWithPythonTricks(R)

    i, j, k = 0, 0, 0 # i - wskaźnik na L, j na R, k na T

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        T[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        T[k] = R[j]
        j += 1
        k += 1

T = [randrange(10) for _ in range(10)]
print(T)
start = time.time()
mergeSortWithPythonTricks(T)
end = time.time()
print(T)
print(end - start)


# [67, 16, 43, 67, 61, 37, 58, 24, 73, 29]
#
# 