from random import randint
def sort(T):
    n = len(T)
    build_heap(T)
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, n, i)
def build_heap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)
def parent(i): return (i - 1) // 2
def left(i): return 2 * i + 1
def right(i): return 2 * i + 2
def heapify(T, n, i):
    l, r, mi = left(i), right(i), i
    if l < n and T[l] > T[mi]: mi = l
    if r < n and T[r] > T[mi]: mi = r
    if mi != i:
        T[mi], T[i] = T[i], T[mi]
        heapify(T, n, mi) 
        
def check_condition(T):
    n = len(T)
    sort(T) # n logn
    for i in range(n - 1): # n^2
        j, k = i + 1, n - 1
        while j < k:
            sum = T[j] + T[k]
            if sum == T[i]: break
            if sum < T[i]: k -= 1
            else: j += 1
        if j == k: return False
    return True

T = [randint(1, 30) for _ in range(20)]
print(T)
print(check_condition(T))