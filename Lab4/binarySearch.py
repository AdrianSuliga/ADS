def quick_sort(T):
    def sort(T, left, right):
        if left >= right: return
        pivot = partition(T, left, right)
        sort(T, left, pivot - 1)
        sort(T, pivot + 1, right)
    return sort(T, 0, len(T) - 1)
def partition(T, left, right):
    pivot = right
    index = left - 1
    for i in range(left, right):
        if T[i] < T[pivot]:
            index += 1
            T[i], T[index] = T[index], T[i]
    index += 1
    T[index], T[pivot] = T[pivot], T[index]
    return index
def binary_search(T, value):
    n = len(T)
    left, right = 0, n - 1
    while True:
        if left > right: break
        pivot = (left + right) // 2
        if T[pivot] == value:
            return pivot
        elif T[pivot] > value:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1


T = [7, 9, 1, 15, 12, 10, 22]
quick_sort(T)
print(T)
print(binary_search(T, 3))