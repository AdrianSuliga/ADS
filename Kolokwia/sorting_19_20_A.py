from random import randint
# Adrian Suliga
# Program używa algorytmu quick_sort do posortowania elementów tablicy względem relacji ,,ładności".
# Złożoność algorytmu szacuję na O(n*logn(n)) gdzie n to długość tablicy wejściowej.
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
            if is_prettier(T, i, pivot):
                ind += 1
                T[i], T[ind] = T[ind], T[i]
        ind += 1
        T[ind], T[pivot] = T[pivot], T[ind]
        return ind
    return sort(T, 0, len(T) - 1)

def is_prettier(T, i, j):
    n = T[i] # nie możemy zniszczyć elementów tablicy T podczas sortowania
    m = T[j] # więc je kopiuję
    digits_n, digits_m = [0 for _ in range(10)], [0 for _ in range(10)]

    while n != 0:
        digits_n[n % 10] += 1
        n //= 10
    while m != 0:
        digits_m[m % 10] += 1
        m //= 10

    ones_cnt = 0
    for i in range(10):
        if digits_n[i] == 1: ones_cnt += 1
        if digits_m[i] == 1: ones_cnt -= 1

    if ones_cnt > 0: return True
    if ones_cnt < 0: return False
    
    multi_cnt = 0
    for i in range(10):
        if digits_n[i] > 1: multi_cnt += 1
        if digits_m[i] > 1: multi_cnt -= 1

    if multi_cnt < 0: return True
    return False

T = [123, 455, 1266, 114577, 2344, 67333]
quick_sort(T)
print(T)