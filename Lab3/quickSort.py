from random import randrange
def quick_sort(T):
    def sort(T, left, right):
        if left < right:
            pivot = partition(T, left, right)
            sort(T, left, pivot - 1)
            sort(T, pivot + 1, right)
    def partition(T, left, right):
        pivot = right
        index = left - 1
        for i in range(left, right):
            if T[i] < T[pivot]:
                index += 1
                T[index], T[i] = T[i], T[index]
        index += 1
        T[pivot], T[index] = T[index], T[pivot]
        return index
    return sort(T, 0, len(T) - 1)

T = [randrange(100) for _ in range(20)]
print(T)
quick_sort(T)
print(T)