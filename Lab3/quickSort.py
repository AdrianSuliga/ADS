from random import randrange

def quick_sort(T):
    def sort(T, left, right):
        if left < right:
            pivot = partition_array(T, left, right)
            sort(T, left, pivot - 1)
            sort(T, pivot + 1, right)

    def partition_array(T, left, right):
        pivot = right
        stored_index = left - 1

        for i in range(left, right):
            if T[i] < T[pivot]:
                stored_index += 1
                T[i], T[stored_index] = T[stored_index], T[i]
        T[pivot], T[stored_index + 1] = T[stored_index + 1], T[pivot]
        return stored_index + 1
    
    return sort(T, 0, len(T) - 1)

T = [randrange(100) for _ in range(10)]
print(T)
quick_sort(T)
print(T)