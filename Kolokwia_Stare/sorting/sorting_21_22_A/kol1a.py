from kol1atesty import runtests
from random import randint
# O(N + 2*nk + nk) = O(N + 2*nk) = O(nk), bo N <= nk

def g(T):
    n = len(T)
    for i in range(n): 
        if not is_palindrome(T[i]):
            T.append(T[i][::-1]) # O(len(T[0]) + len(T[1]) + ... ) = O(N) na rozszerzenie tablicy o odwrotności wszystkich napisów
    quick_sort(T) # O(n logn) na posortowanie
    #radix_sort(T)
    return longest_subsequence(T) # O(nk) na znalezienie najdłuższego podciągu
    
def is_palindrome(s):
    n = len(s)
    i, j = 0, n - 1
    while i < j:
        if s[i] != s[j]: return False
        i += 1
        j -= 1
    return True

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

def longest_subsequence(T):
    max_len = -1
    i, j = 0, 0
    n = len(T)
    while j < n:
        while j < n and are_the_same(T, i, j):
            j += 1
        max_len = max(max_len, j - i)
        i = j
    return max_len

def are_the_same(T, i, j):
    n, m = len(T[i]), len(T[j])
    if n != m: return False
    for k in range(n):
        if T[i][k] != T[j][k]: return False
    return True

def find_max_length(T):
    max_len = -float('inf')
    for i in range(len(T)): max_len = max(max_len, len(T[i]))
    return max_len

def radix_sort(T):
    k = find_max_length(T)
    for i in range(k - 1, -1, -1):
        counting_sort(T, i)

def counting_sort(T, ind):
    n = len(T)
    C = [0 for _ in range(27)]
    B = [None for _ in range(n)]

    Len_Arr = [len(T[i]) for i in range(n)]

    for i in range(n):
        if Len_Arr[i] - 1 < ind:
            C[26] += 1
        else:
            C[ord(T[i][ind]) - ord('a')] += 1
    
    for i in range(1, 27): C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        if Len_Arr[i] - 1 < ind:
            B[C[26] - 1] = T[i]
            C[26] -= 1
        else:
            B[C[ord(T[i][ind]) - ord('a')] - 1] = T[i]
            C[ord(T[i][ind]) - ord('a')] -= 1

    for i in range(n): T[i] = B[i]

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
"""T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
print(g(T))"""