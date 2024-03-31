from random import randint
# Adrian Suliga
# Program sortuje tablicę w złożoności nlogn, następnie zwraca wartości od indeksów p. do q. włącznie. Szacowana złożoność: O(n logn + q - p + 1) przy czym
# nlogn dominuje q - p + 1, zatem ostatecznie mamy O(n logn)
def selectionV1(T, p, q):
    quick_sort(T)
    result = [0 for _ in range(q - p + 1)]
    print(T)
    it = 0
    for i in range(p, q + 1):
        result[it] = T[i]
        it += 1
    return result
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
            if T[i] < T[pivot]:
                ind += 1
                T[i], T[ind] = T[ind], T[i]
        ind += 1
        T[ind], T[pivot] = T[pivot], T[ind]
        return ind
    return sort(T, 0, len(T) - 1)

# Adrian Suliga
# Program wykorzystuje algorytm quick_select() aby znaleźć wzrost żołnierza na pozycji p, p + 1, p + 2, ..., q
# Szacowana złożoność: O((q - p + 1) * n), warto zauważyć że przy odpowiednio dużym q - p, na przykład rzedu c * n gdzie
# c to jakaś stała, ten algorytm będzie miał złożoność kwadratową, co czyni go w niektórych przypadkach gorszym niż O(nlogn)

def selectionV2(T, p, q):
    result = [0 for _ in range(q - p + 1)]
    n = len(T)
    for i in range(q - p + 1):
        result[i] = quick_select(T, 0, n - 1, i + p)
    return result

def quick_select(T, left, right, ind):
    if left >= right: return T[left]
    pivot = randint(left, right)
    pivot = partition(T, left, right, pivot)
    if ind == pivot: return T[pivot]
    if ind < pivot: right = pivot - 1
    else: left = pivot + 1
    return quick_select(T, left, right, ind)

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

T = [randint(150, 210) for _ in range(30)]
print(T)
print(selectionV2(T, 4, 6))
quick_sort(T)
print(T)