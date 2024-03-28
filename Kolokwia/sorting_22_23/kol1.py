from kol1testy import runtests

# Adrian Suliga
# Algorytm szuka w każdym z n - p + 1 przedziałów k. największego elementu, następnie dodaje go do będącej wynikiem programu sumy.
# W celu znalezienia k. największego elementu używam algorytmu quick_select. Pracuje on zawsze na tablicach rozmiaru p, co daje złożoność O(p)
# Wywołanie quick_select zagnieżdżone jest w pętli for, więc ostateczną złożoność czasową algorytmu oceniam na O(np). Pamięciową zaś na O(p) z
# powodu użycia pomocniczej tablicy

def ksum(T, k, p):
    sum, n = 0, len(T)

    for i in range(n - p + 1):
        sum += k_th_largest(T, i, k, p)

    return sum

def k_th_largest(T, index, k, p):
    A = T[index:(index + p)]
    return quick_select(A, k - 1, 0, len(A) - 1)

def quick_select(T, k, left, right):
    if left == right: return T[left]

    pivot = partition(T, left, right)

    if pivot == k: return T[k]
    elif pivot < k: left = pivot + 1
    else: right = pivot - 1

    return quick_select(T, k, left, right)

def partition(T, left, right):
    pivot = (left + right) // 2
    T[pivot], T[right] = T[right], T[pivot]
    pivot = right
    ind = left - 1
    for i in range(left, right):
        if T[i] > T[pivot]:
            ind += 1
            T[i], T[ind] = T[ind], T[i]
    ind += 1
    T[pivot], T[ind] = T[ind], T[pivot]
    return ind

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
