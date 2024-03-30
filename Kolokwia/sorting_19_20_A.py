from random import randint
def quick_sort(T):
    def sort(T, left, right):
        if left > right: return
        pivot = randint(left, right)
        pivot = partition(T, left, right, pivot)
        sort(T, left, pivot - 1)
        sort(T, pivot + 1, right)
    def partition(T, left, right, p_index):
        pivot = right
        T[p_index], T[right] = T[right], T[p_index]
        ind = left - 1
        for i in range(left, right):
            if is_prettier(T, i, ind):
                ind += 1
                T[i], T[ind] = T[ind], T[i]
        ind += 1
        T[ind], T[pivot] = T[pivot], T[ind]
        return ind
    return sort(T, 0, len(T) - 1)
def is_prettier(T, i, j):
    pass