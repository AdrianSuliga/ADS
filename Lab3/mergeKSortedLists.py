# sort k sorted lists (n elements in total) in O(n logk)
# 1. use heap
# 2. use ,,merge sort" like sorting
def build_heap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)

def heapify(T, n, i):
    l, r = left(i), right(i)
    mi = i
    if l < n and T[l][0] < T[mi][0]: mi = l
    if r < n and T[r][0] < T[mi][0]: mi = r

    if mi != i:
        T[mi], T[i] = T[i], T[mi]
        heapify(T, n, mi)

def left(i): return 2 * i + 1
def right(i): return 2 * i + 2
def parent(i): return (i - 1) // 2

def merge(T):
    k = len(T)
    result = []
    heap = []
    index_count = [0 for _ in range(k)]
    
    for i in range(k):
        heap.append((T[i][index_count[i]], i))
    
    build_heap(heap)
    while len(heap) > 0:
        result.append(heap[0][0])
        index_count[heap[0][1]] += 1
        if index_count[heap[0][1]] >= len(T[heap[0][1]]):
            heap[0], heap[-1] = heap[-1], heap[0]   
            heap.pop() 
        else:
            heap[0] = T[heap[0][1]][index_count[heap[0][1]]], heap[0][1]
        heapify(heap, len(heap), 0)

    return result

T = [[10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33, 40, 50, 60], [1, 5, 15, 18, 19, 19, 25, 100, 1000]]
print(merge(T))