from zad3testy import runtests
from random import randint
def strong_string(T):
    n = len(T)
    for i in range(n): 
        if not is_palindrome(T[i]):
            T.append(T[i][::-1])
    quick_sort(T)
    return longest_subsequence(T)

def longest_subsequence(T):
    n = len(T)
    max_len = -1
    i, j = 0, 0
    while j < n:
        while j < n and T[i] == T[j]:
            j += 1
        max_len = max(max_len, j - i)
        i = j
    return max_len

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
        p_index = randint(left, right)
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
                T[ind], T[i] = T[i], T[ind]
        ind += 1
        T[ind], T[pivot] = T[pivot], T[ind]
        return ind
    return sort(T, 0, len(T) - 1)


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
