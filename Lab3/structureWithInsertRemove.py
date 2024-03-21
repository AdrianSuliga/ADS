# insert in logn - easy
# removal in logn - two heaps. Each heap (min and max) has tuples as elements.
# min tuples: (value, pos_in_max_heap)
# max tuples: (value, pos_in_min_heap) 
from random import randint

def parent(i): return (i - 1) // 2
def left(i): return 2 * i + 1
def right(i): return 2 * i + 2

def build_min_heap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify_min(T, n, i)
def build_max_heap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify_max(T, n, i)

def heapify_min(T, n, i):
    l, r = left(i), right(i)
    mi = i

    if l < n and T[l][0] < T[mi][0]: mi = l
    if r < n and T[r][0] < T[mi][0]: mi = r

    if mi != i:
        T[i], T[mi] = T[mi], T[i]
        heapify_min(T, n, mi)

def heapify_max(T, n, i):
    l, r = left(i), right(i)
    mi = i

    if l < n and T[l][0] > T[mi][0]: mi = l
    if r < n and T[r][0] > T[mi][0]: mi = r

    if mi != i:
        T[i], T[mi] = T[mi], T[i]
        heapify_max(T, n, mi)

def insert(min_heap, max_heap, val):
    min_heap.append(val)
    max_heap.append(val)
    
    min_i = len(min_heap) - 1
    max_i = len(max_heap) - 1
    while min_i > 0 and min_heap[parent(min_i)][0] > min_heap[min_i][0]:
        min_heap[parent(min_i)], min_heap[min_i] = min_heap[min_i], min_heap[parent(min_i)]
        min_i = parent(min_i)
    while max_i > 0 and max_heap[parent(max_i)][0] < max_heap[max_i][0]:
        max_heap[parent(max_i)], max_heap[max_i] = max_heap[max_i], max_heap[parent(max_i)]
        max_i = parent(max_i)

def remove_min(min_heap:list, max_heap:list):
    max_heap[-1], max_heap[min_heap[0][1]] = max_heap[min_heap[0][1]], max_heap[-1]
    max_heap.pop()
    heapify_max(max_heap, len(max_heap), min_heap[0][1])

    min_heap[0], min_heap[-1] = min_heap[-1], min_heap[0]
    min_heap.pop()
    heapify_min(min_heap, len(min_heap), 0)

def remove_max(min_heap:list, max_heap:list):
    min_heap[-1], min_heap[max_heap[0][1]] = min_heap[max_heap[0][1]], min_heap[-1]
    min_heap.pop()
    heapify_max(min_heap, len(min_heap), max_heap[0][1])

    max_heap[0], max_heap[-1] = max_heap[-1], max_heap[0]
    max_heap.pop()
    heapify_min(max_heap, len(max_heap), 0)

def prepare_heaps(T):
    n = len(T)
    min_heap = [(T[i], i) for i in range(n)]
    max_heap = [(T[i], i) for i in range(n)]

    build_max_heap(max_heap)
    build_min_heap(min_heap)

    for i in range(n):
        for j in range(n):
            if min_heap[j][0] == max_heap[i][0]:
                max_heap[i] = max_heap[i][0], j
            if min_heap[i][0] == max_heap[j][0]:
                min_heap[i] = min_heap[i][0], j
    return min_heap, max_heap
    
T = [7, 3, 100, 49, 50, 4, 83, 11, 58, 17]
min_heap, max_heap = prepare_heaps(T)