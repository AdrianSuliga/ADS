from egzP2btesty import runtests
from math import log10

def kryptograf(D, Q):
    n, q = len(D), len(Q)
    m, maxstr = -1, ""
    for i in range(n):
        D[i] = D[i][::-1]
        if len(D[i]) > len(maxstr): 
            m = len(D[i])
            maxstr = D[i]
    for i in range(q):
        Q[i] = Q[i][::-1]

    D = radix_sort(D, m)

    result = 1
    for i in range(q):
        low = binary_search(Q[i], D, 0, n - 1)
        high = binary_search(Q[i] + "2", D, 0, n - 1)
        result *= high - low

    return log10(result)

def radix_sort(D, m):
    n = len(D)
    
def binary_search(word, D, left, right):
    if left > right: return left
    pivot = (left + right) // 2
    if word <= D[pivot]:
        return binary_search(word, D, left, pivot - 1)
    else: return binary_search(word, D, pivot + 1, right)

# Adrian Suliga
# Algorytm odwraca wszystkie napisy w D i Q, sortuje D i szuka
# na ile sposobów możemy dopasować napisy z Q do D, ale patrzymy teraz
# na prefixy. Zastosowanie sortowania pozwala nam na użycie szukania binarnego
# do zdeterminowania ilu napisów prefixem może być dany napis z Q. Szacuję złożoność czasową algorytmu na
# O(n^2logn + qmlogn), a pamięciową na O(logn)
"""def kryptograf( D, Q ):
    n, q = len(D), len(Q) # odwracamy wszystkie napisy w D i Q
    for i in range(n): # a następnie jest sortujemy
        D[i] = D[i][::-1] 
    for i in range(q):
        Q[i] = Q[i][::-1]
    D.sort()
    
    # teraz szukamy dla każdego napisu w Q ilu
    # napisów może on być prefiksem
    result = 1
    for i in range(q):
        low = binary_search(Q[i], D, 0, n - 1)
        high = binary_search(Q[i] + "2", D, 0, n - 1)
        result *= (high - low)
    
    return log10(result)

def binary_search(word, D, left, right):
    if left > right: return left
    pivot = (left + right) // 2

    if word <= D[pivot]:
        return binary_search(word, D, left, pivot - 1)
    else:
        return binary_search(word, D, pivot + 1, right)"""

# O(mnq)
"""def kryptograf( D, Q ):    
    result = 1
    n, q = len(D), len(Q)
    L = [len(D[i]) for i in range(n)]

    for i in range(q):
        if Q[i] == "":
            result *= n
            continue
        w, sum = len(Q[i]), 0
        for j in range(n):
            if Q[i] == D[j][L[j] - w:]: sum += 1
        result *= sum

    return log10(result)"""

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
#runtests(kryptograf, all_tests = 2)
D = ["1100", "100", "0", "1111", "1101"]
Q = ["", "1", "11", "0", "1101"]
print(kryptograf(D, Q))