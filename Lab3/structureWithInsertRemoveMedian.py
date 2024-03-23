from random import randint
class Extra_Heap:
    def __init__(self):
        self.HeapMax = []
        self.HeapMin = []
        self.median = None
        self.size = 0

def parent(i): return (i - 1) // 2
def left(i): return 2 * i + 1
def right(i): return 2 * i + 2

def build_heap_max(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify_max(T, n, i)
def build_heap_min(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify_min(T, n, i)

def heapify_max(T, n, i):
    l, r = left(i), right(i)
    mi = i

    if l < n and T[l] > T[mi]: mi = l
    if r < n and T[r] > T[mi]: mi = r

    if mi != i:
        T[mi], T[i] = T[i], T[mi]
        heapify_max(T, n, mi)
def heapify_min(T, n, i):
    l, r = left(i), right(i)
    mi = i

    if l < n and T[l] < T[mi]: mi = l
    if r < n and T[r] < T[mi]: mi = r

    if mi != i:
        T[mi], T[i] = T[i], T[mi]
        heapify_min(T, n, mi)

def heapify_max_up(heap, i):
    while i > 0 and heap[i] > heap[parent(i)]:
        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
        i = parent(i)
def heapify_min_up(heap, i):
    while i > 0 and heap[i] < heap[parent(i)]:
        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
        i = parent(i)

def insert(H:Extra_Heap, val:int):
    n = H.size
    if n == 0:
        H.median = val
    elif n == 1:
        if val <= H.median:
            H.HeapMax.append(val)
            H.HeapMin.append(H.median)
        else:
            H.HeapMax.append(H.median)
            H.HeapMin.append(val)
        H.median = None
    elif n % 2 == 0:
        if H.HeapMax[0] <= val <= H.HeapMin[0]:
            H.median = val
        elif val < H.HeapMax[0]:
            H.median = H.HeapMax[0]
            H.HeapMax[0] = val
            heapify_max(H.HeapMax, len(H.HeapMax), 0)
        elif H.HeapMin[0] < val:
            H.median = H.HeapMin[0]
            H.HeapMin[0] = val
            heapify_min(H.HeapMin, len(H.HeapMin), 0)
    elif n % 2 == 1:
        if H.median <= val:
            H.HeapMax.append(H.median)
            heapify_max_up(H.HeapMax, len(H.HeapMax) - 1)
            H.HeapMin.append(val)
            heapify_min_up(H.HeapMin, len(H.HeapMin) - 1)
        elif val < H.median:
            H.HeapMax.append(val)
            heapify_max_up(H.HeapMax, len(H.HeapMax) - 1)
            H.HeapMin.append(H.median)
            heapify_min_up(H.HeapMin, len(H.HeapMin) - 1)
        H.median = None
    H.size += 1

def extract_median(H:Extra_Heap):
    result = 0
    if H.median == None:
        result = (H.HeapMax[0] + H.HeapMin[0]) / 2
        H.HeapMax[0], H.HeapMax[-1] = H.HeapMax[-1], H.HeapMax[0]
        H.HeapMax.pop()
        heapify_max(H.HeapMax, len(H.HeapMax), 0)
        H.HeapMin[0], H.HeapMin[-1] = H.HeapMin[-1], H.HeapMin[0]
        H.HeapMin.pop()
        heapify_min(H.HeapMin, len(H.HeapMin), 0)
    else:
        result = H.median
        H.median = None
        H.size -= 1
    return result

H = Extra_Heap()

insert(H, 11)
insert(H, 16)
insert(H, 13)
insert(H, 18)
insert(H, 20)
insert(H, 21)
insert(H, 17)
insert(H, 19)
print(H.HeapMax, H.median, H.HeapMin)
print(extract_median(H))