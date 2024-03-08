"""
implement merge sort on array
"""
from random import randrange
import time
def mergeSortClean(T):
    n = len(T)
    if n == 1:
        return
    
    pivot = n // 2
    L = [T[i] for i in range(pivot)]
    R = [T[i] for i in range(pivot, n)]
    """
    L = T[:pivot]
    R = T[pivot:]
    """
    
    mergeSortClean(L)
    mergeSortClean(R)

    i, j, k = 0, 0, 0
    while i < n // 2 and j < n - n // 2:
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1
        k += 1
    while i < n // 2:
        T[k] = L[i]
        i += 1
        k += 1
    while j < n - n // 2:
        T[k] = R[j]
        j += 1
        k += 1

T = [randrange(100) for _ in range(1000000)]
start = time.time()
mergeSortClean(T)
end = time.time()
print(end - start)
