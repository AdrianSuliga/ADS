from zad2testy import runtests
from random import randint

def ksum(T, k, p):
    sum = 0
    n = len(T)
    for i in range(n - p + 1):
        sum += kth_largest(T, i, i + p - 1, k)
    return sum

def kth_largest(T, left, right, k):
    A = [T[i] for i in range(left, right + 1)]
    return quick_select(A, 0, right - left, k - 1)

def quick_select(T, left, right, k):
    if left == right:
        return T[left]
    
    pInd = randint(left, right)
    pInd = partition(T, left, right, pInd)

    if k == pInd:
        return T[k]
    elif k < pInd:
        return quick_select(T, left, pInd - 1, k)
    else:
        return quick_select(T, pInd + 1, right, k)
    
def partition(T, left, right, pInd):
    pivot = right
    T[pInd], T[right] = T[right], T[pInd]
    index = left - 1

    for i in range(left, right):
        if T[i] >= T[pivot]:
            index += 1
            T[i], T[index] = T[index], T[i]

    index += 1
    T[pivot], T[index] = T[index], T[pivot]
    return index

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )