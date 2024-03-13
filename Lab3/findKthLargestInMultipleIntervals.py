# naive approach for offline 2 - O(nk logp) passes only 5/10 tests
# algorithms searches for k. largest element using max heaps
def ksum(T, k, p):
    n = len(T)
    sum = 0
    for i in range(n - p + 1):
        factor = kth_largest(T, i, i + p - 1, k)
        sum += factor
    return sum

def kth_largest(T, start, end, k):
    heap = T[start:(end + 1)]
    return largest(heap, k)

def largest(heap, k):
    n = len(heap)
    build_heap(heap)
    for i in range(k - 1):
        heap[0], heap[n - 1] = heap[n - 1], heap[0]
        n -= 1
        heapify(heap, n, 0)
    return heap[0]

def build_heap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)

def heapify(T, n, i):
    l, r = left(i), right(i)
    mi = i

    if l < n and T[l] > T[mi]:
        mi = l
    if r < n and T[r] >  T[mi]:
        mi = r

    if i != mi:
        T[i], T[mi] = T[mi], T[i]
        heapify(T, n, mi)

def parent(i):
    return (i - 1) // 2
def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2