from egzP4btesty import runtests 

# Adrian Suliga
# Algorytm dla każdego wierzchołka tablicy T oblicza wartości jego poprzednika i następnika
# następnie sprawdza czy wierzchołek jest piękny. Szacuję złożoność czasową algorytmu na
# O(qh), a pamięciową na O(h) - wywołania rekurencyjne.

class Node:
    def __init__(self, key, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.x = None

def sol(root:Node, T:list[Node]) -> int:
    result = 0
    for node in T:
        prev = node_prev(node) # obliczamy poprzednik
        next = node_next(node) # obliczemy następnik
        if prev is None or next is None: continue
        if prev + next == 2 * node.key: result += node.key
    
    return result

def node_prev(node:Node):
    if node.left is not None: # jeśli ma lewe poddrzewo, to
        return max_val(node.left) # idziemy maksymalnie w dół na lewo
    
    parent_node = node.parent # w przeciwnym wypadku musimy szukać
    while parent_node.left == node: # poprzednika wśród parentów
        node = parent_node
        parent_node = parent_node.parent
    return parent_node.key

def node_next(node:Node):
    if node.right is not None:
        return min_val(node.right)

    parent_node = node.parent
    while parent_node.right == node:
        node = parent_node
        parent_node = parent_node.parent
    return parent_node.key

def max_val(node:Node):
    ptr = node
    while ptr.right is not None:
        ptr = ptr.right
    return ptr.key

def min_val(node:Node):
    ptr = node
    while ptr.left is not None:
        ptr = ptr.left
    return ptr.key

# Adrian Suliga
# Algorytm wyznacza z drzewa tablicę posortowanych wartości kluczy wierzchołków, następnie
# dla każdego wierzchołka tablicy T wyszukujemy w posortowanej tablicy jego indeks, dzięki
# czemu jesteśmy w stanie łatwo sprawdzić jego poprzednika i następnika. Szacuję złożoność
# czasową algorytmu na O(n + qlogn), a pamięciową na O(n)
"""def sol(root:Node, T:list[Node]):
    A, result = [], 0
    travel(root, A)
    n = len(A)

    for node in T:
        x = bin_search(node.key, A, 0, n - 1)
        if A[x - 1] + A[x + 1] == 2 * A[x]: result += A[x]

    return result

def travel(node:Node, T:list) -> None:
    if node.left is not None:
        travel(node.left, T)
    T.append(node.key)
    if node.right is not None:
        travel(node.right, T)

def bin_search(val, T, left, right) -> int:
    if left > right: return -1
    pivot = (left + right) // 2

    if T[pivot] == val: return pivot
    elif T[pivot] < val: return bin_search(val, T, pivot + 1, right)
    else: return bin_search(val, T, left, pivot - 1)"""

runtests(sol, all_tests = True)
