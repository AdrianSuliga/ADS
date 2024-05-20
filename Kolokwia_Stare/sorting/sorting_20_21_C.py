# sortowanie tablicy liczb wygenerowanych z pewnego rozkładu
from random import randint
from math import ceil
def quick_sort(T):
    def sort(T, left, right):
        if left > right: return
        pivot = randint(left, right)
        pivot = partition(T, left, right, pivot)
        sort(T, left, pivot - 1)
        sort(T, pivot + 1, right)
    def partition(T, left, right, p_index):
        pivot = right
        T[p_index], T[right] = T[right], T[p_index]
        ind = left - 1
        for i in range(left, right):
            if T[i] < T[pivot]:
                ind += 1
                T[i], T[ind] = T[ind], T[i]
        ind += 1
        T[ind], T[pivot] = T[pivot], T[ind]
        return ind
    return sort(T, 0, len(T) - 1)

def bucket_sort(T, P):
    n, k = len(T), 0
    buckets = [[] for _ in range(n - 1)]

    for i in range(n):
        buckets[int(T[i]) - 1].append(T[i])
    for i in range(n - 1):
        selection_sort(buckets[i])
    for i in range(n - 1):
        for j in range(len(buckets[i])):
            T[k] = buckets[i][j]
            k += 1

def selection_sort(T):
    n = len(T)
    for i in range(1, n):
        to_insert = T[i]
        j = i - 1
        while j > -1 and T[j] > to_insert:
            T[j + 1], T[j] = T[j], T[j + 1]
            j -= 1
        T[j + 1] = to_insert


P = [(1, 5, 0.75) , (4, 8, 0.25)]
T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
bucket_sort(T, P)
print(T)