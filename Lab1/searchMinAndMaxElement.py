"""
find smallest and largest number in the array
"""
from random import randrange
def lookForSmallestAndGreatest(T):
    mini, maks = float('inf'), -float('inf')
    for i in range(0, len(T), 2):
        if (T[i] < T[i+1]):
            if T[i] < mini:
                mini = T[i]
            if T[i+1] > maks:
                maks = T[i+1]
        else:
            if T[i+1] < mini:
                mini = T[i+1]
            if T[i] > maks:
                maks = T[i]
    return (mini, maks)


T = [randrange(10, 100) for _ in range(100)]
print(T)
print(lookForSmallestAndGreatest(T))