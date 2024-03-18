# n log(n) + n 2log(n) = 3n log(n) = n log(n) solution

def dominance(P:list):
    n = len(P)

    X_sorted = P.copy()
    Y_sorted = P.copy()

    merge_sort_X(X_sorted)
    merge_sort_Y(Y_sorted)

    max_dominance = -float('inf')

    for i in range(len(P)):
        domX = binary_search_X(X_sorted, P[i], 0, n - 1)
        domY = binary_search_Y(Y_sorted, P[i], 0, n - 1)
        dom = min(domX, domY)
        max_dominance = max(max_dominance, dom)

    return max_dominance

def binary_search_X(T, value, left, right):
    if left > right: return -1
    pivot = (left + right) // 2
    if T[pivot] == value:
        return pivot
    elif T[pivot][0] < value[0]:
        left = pivot + 1
    else:
        right = pivot - 1
    return binary_search_X(T, value, left, right)

def binary_search_Y(T, value, left, right):
    if left > right: return -1
    pivot = (left + right) // 2
    if T[pivot] == value:
        return pivot
    elif T[pivot][1] < value[1]:
        left = pivot + 1
    else:
        right = pivot - 1
    return binary_search_Y(T, value, left, right)

def merge_sort_X(T):
    n = len(T)
    if n == 1: return
    pivot = n // 2
    L = T[:pivot]
    R = T[pivot:]
    merge_sort_X(L)
    merge_sort_X(R)

    i, j, k = 0, 0, 0
    while i < pivot and j < n - pivot:
        if L[i][0] <= R[j][0]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1
        k += 1
    while i < pivot:
        T[k] = L[i]
        k += 1
        i += 1
    while j < n - pivot:
        T[k] = R[j]
        j += 1
        k += 1
    
def merge_sort_Y(T):
    n = len(T)
    if n == 1: return
    pivot = n // 2
    L = T[:pivot]
    R = T[pivot:]
    merge_sort_Y(L)
    merge_sort_Y(R)

    i, j, k = 0, 0, 0
    while i < pivot and j < n - pivot:
        if L[i][1] <= R[j][1]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1
        k += 1
    while i < pivot:
        T[k] = L[i]
        k += 1
        i += 1
    while j < n - pivot:
        T[k] = R[j]
        j += 1
        k += 1

"""P = [(2, 7), (6, 7), (6, 3), (10, 9), (2, 3), (10, 5), (10, 1), (4, 3), (10, 7), (4, 7)]
print(dominance(P))"""