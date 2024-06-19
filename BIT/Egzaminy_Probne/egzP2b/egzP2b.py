from egzP2btesty import runtests
from math import log10

# Adrian Suliga
# Algorytm buduje drzewo BST, którego węzłami są napisy złożone z 0 i 1
# Każdy node przechowuje dodatkowo liczbę napisów w swoim poddrzewie, które dodaliśmy
# Wynikiem zadania jest zliczenie wszystkich tych przechowywanych wartości.
# Szacuję złożoność czasową algorytmu na O(mn + mq), a pamięciową na O(mn)

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.x = 0

def kryptograf(D, Q):
    root, result = Node(), 0

    for i in range(len(D)):
        insert_node(D[i], root)

    for i in range(len(Q)):
        result += log10(calc_prefix(Q[i], root))

    return result

def calc_prefix(word:str, node:Node):
    if word == "": return node.x
    if word[-1] == '0': return calc_prefix(word[:-1], node.right)
    else: return calc_prefix(word[:-1], node.left)

def insert_node(word:str, node:Node):
    node.x += 1
    if word == "": return

    if word[-1] == '0':
        if node.right == None: node.right = Node()
        insert_node(word[:-1], node.right)
    else:
        if node.left == None: node.left = Node()
        insert_node(word[:-1], node.left)

# Adrian Suliga
# Algorytm jak niżej ale do sortowania używam radix sorta, co pozwala
# osiągnąć złożoność czasową O(nm + qmlogn), a pamięciową O(n)
"""def kryptograf(D, Q):
    n, q = len(D), len(Q)
    m = -1
    for i in range(n):
        D[i] = D[i][::-1]
        m = max(m, len(D[i]))
    for i in range(q):
        Q[i] = Q[i][::-1]

    radix_sort(D, m)

    result = 1
    for i in range(q):
        low = binary_search(Q[i], D, 0, n - 1)
        high = binary_search(Q[i] + "2", D, 0, n - 1)
        result *= (high - low)

    return log10(result)

def radix_sort(D, m):
    for i in range(m - 1, -1, -1):
        c_sort(i, D) # sort strings in D by their i. char

def c_sort(ind, D):
    n = len(D)
    B = [None for _ in range(n)]
    C = [0 for _ in range(3)]

    for i in range(n):
        if len(D[i]) - 1 < ind:
            C[0] += 1
        else:
            C[ord(D[i][ind]) - ord('0') + 1] += 1

    C[1] += C[0]
    C[2] += C[1]

    for i in range(n - 1, -1, -1):
        if len(D[i]) - 1 < ind:
            B[C[0] - 1] = D[i]
            C[0] -= 1
        else:
            B[C[ord(D[i][ind]) - ord('0') + 1] - 1] = D[i]
            C[ord(D[i][ind]) - ord('0') + 1] -= 1
    
    for i in range(n): D[i] = B[i]
    
def binary_search(word, D, left, right):
    if left > right: return left
    pivot = (left + right) // 2
    if word <= D[pivot]: return binary_search(word, D, left, pivot - 1)
    else: return binary_search(word, D, pivot + 1, right)"""

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
runtests(kryptograf, all_tests = 3)
