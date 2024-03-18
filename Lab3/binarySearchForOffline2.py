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
    mi = i

    if l < n and T[l] < T[mi]: mi = l
    if r < n and T[r] < T[mi]: mi = r

    if i != mi:
        T[mi], T[i] = T[i], T[mi]
        heapify(T, n, mi)

def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2
def parent(i):
    return (i - 1) // 2

def ksum(T, k, p):
    n = len(T)
    sum = 0
    A = T[:p]
    heap_sort(A)
    for i in range(n - p + 1):
        sum += A[k-1]
        if i + p < n:
            binary_insert(A, T[i + p])
        A.remove(T[i])
    return sum

def binary_insert(T:list, val):
    def find(T, ind, val, left, right, result):
        if left > right: return result
        if T[ind] <= val:
            right = ind - 1
        else:
            result = ind
            left = ind + 1
        return find(T, (left + right) // 2, val, left, right, result)

    if T[0] < val:
        T.insert(0, val)
        return
    if T[-1] > val:
        T.append(val)
        return
    
    n = len(T)
    res_ind = find(T, n // 2, val, 0, n - 1, n // 2)
    T.insert(res_ind + 1, val)

T =  [7, 9, 1, 5, 8, 6, 2, 12]
k =  4
p =  5
print(ksum(T, k, p))