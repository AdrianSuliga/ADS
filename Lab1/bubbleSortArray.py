"""
implement bubble sort on array T
"""
from random import randrange
def bubbleSortV1(T):
    n = len(T)
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
def bubbleSortV2(T):
    n = len(T)
    for i in range(n - 1, -1, -1):
        for j in range(1, i + 1):
            if T[j] < T[j - 1]:
                T[j - 1], T[j] = T[j], T[j - 1]
T = [4,3,2,1]
bubbleSortV1(T)
print(T)
T = [4, 3, 2, 1]
bubbleSortV2(T)
print(T)