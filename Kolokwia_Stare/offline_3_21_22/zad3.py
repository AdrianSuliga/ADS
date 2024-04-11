from zad3testy import runtests

def SortTab(T,P):
    quick_sort(T)
    return T

def quick_sort(T):
    def sort(T, left, right):
        if left > right: return
        p_index = (left + right) // 2
        pivot = partition(T, left, right, p_index)
        sort(T, left, pivot - 1)
        sort(T, pivot + 1, right)
    def partition(T, left, right, p_index):
        pivot = right
        T[p_index], T[right] = T[right], T[p_index]
        ind = left - 1
        for i in range(left, right):
            if T[i] < T[pivot]:
                ind += 1
                T[i], T[ind] = T[ind], T[i]
        ind += 1
        T[ind], T[pivot] = T[pivot], T[ind]
        return ind
    return sort(T, 0, len(T) - 1)

runtests( SortTab )