"""
implement merge sort on array
"""
from random import randrange
import time
def mergeSortClean(T, start, end):
    if start >= end:
        return
    pivot = (end+start) // 2
    mergeSortClean(T, start, pivot)
    mergeSortClean(T, pivot + 1, end)
    merge(T, start, pivot, end)

def merge(T, start, pivot, end):
    n1, n2 = pivot - start + 1, end - pivot
    L, R = [T[i + start] for i in range(n1)], [T[pivot + i + 1] for i in range(n2)]
    i, j, k = 0, 0, start
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        T[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        T[k] = R[j]
        j += 1
        k += 1

def mergeSort(T):
    n = len(T)
    if n <= 1:
        return
    
    pivot = n // 2
    L = T[:pivot]
    R = T[pivot:]
    
    mergeSort(L)
    mergeSort(R)

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

T = [randrange(10) for _ in range(1000000)]
n = len(T)
start = time.time()
mergeSortClean(T, 0, n - 1)
end = time.time()
print(T)
print(end - start)
