def build_heap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)

def heapify(T, n, i):
    l, r = left(i), right(i)
    mi = i
    
    if l < n and T[l] > T[mi]:
        mi = l
    if r < n and T[r] > T[mi]:
        mi = r

    if i != mi:
        T[i], T[mi] = T[mi], T[i]
        heapify(T, n, mi)

def parent(i):
    return (i - 1) // 2
def left(i):
    return 2*i + 1
def right(i):
    return 2*i + 2

def kth_largest(T:list, k:int):
    n = len(T)
    heap = T.copy()
    build_heap(heap)
    for i in range(k - 1):
        heap[0], heap[n - 1] = heap[n - 1], heap[0]
        n -= 1
        heapify(heap, n, 0)
    return heap[0]

T = [7, 9, 1, 5, 8, 6, 2, 12]
print(T)
print(kth_largest(T, 6))
print(T)