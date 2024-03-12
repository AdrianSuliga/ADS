from random import randrange
import time
def heap_sort(T):
    n = len(T)
    build_heap(T)
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, i, 0)

def build_heap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)

def heapify(T, n, i):
    l, r = left(i), right(i)
    max_ind = i

    if l < n and T[l] > T[max_ind]:
        max_ind = l
    if r < n and T[r] > T[max_ind]:
        max_ind = r

    if max_ind != i:
        T[i], T[max_ind] = T[max_ind], T[i]
        heapify(T, n, max_ind)

def left(i):
    return 2*i + 1
def right(i):
    return 2*i + 2
def parent(i):
    return (i - 1) // 2


T = [randrange(100) for _ in range(1000000)]

start = time.time()
heap_sort(T)
end = time.time()
print(end - start)