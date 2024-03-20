from random import randint
def build_heap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)
def heapify(T, n, i):
    l, r = left(i), right(i)
    mi = i
    if l < n and T[l] > T[mi]: mi = l
    if r < n and T[r] > T[mi]: mi = r

    if mi != i:
        T[mi], T[i] = T[i], T[mi]
        heapify(T, n, mi)

def left(i): return 2 * i + 1
def right(i): return 2 * i + 2
def parent(i): return (i - 1) // 2

def check(T, n, i):
    l, r = left(i), right(i)

    if l < n and T[l] > T[i]: return False
    if r < n and T[r] > T[i]: return False
    if l >= n and r >= n: return True

    return check(T, n, l) and check(T, n, r)

T = [randint(0, 100) for _ in range(20)]
print(T)
build_heap(T)
print(T)