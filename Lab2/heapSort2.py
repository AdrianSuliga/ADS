from random import randrange
def heap_sort(T):
    n = len(T)
    build_heap(T)
    for i in range(n - 1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, i, 0)

def build_heap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)

def heapify(T, n, i):
    l, r, mi = left(i), right(i), i
    if l < n and T[l] > T[mi]:
        mi = l
    if r < n and T[r] > T[mi]:
        mi = r
    if mi != i:
        T[mi], T[i] = T[i], T[mi]
        heapify(T, n, mi)

def parent(i):
    return (i - 1) // 2
def left(i):
    return 2*i + 1
def right(i):
    return 2*i + 2

T = [randrange(100) for _ in range(10)]
print(T)
heap_sort(T)
print(T)