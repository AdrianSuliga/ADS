from egzP5btesty import runtests 
from math import inf

# Adrian Suliga
# Algorytm tworzy z listy połączeń listę krawędzi w czasie O(ElogE) czyli O(ElogV)
# a następnie znajduje na nim wszystkie punkty artykulacji w czasie O(E + V). Szacuję
# złożoność czasową algorytmu jako O(ElogV), a pamięciową jak O(E + V)

def koleje(B:list) -> int:
    G = list_form(B)
    n = len(G)
    is_art = [False for _ in range(n)]
    discovery = [None for _ in range(n)]
    parent = [None for _ in range(n)]
    low = [None for _ in range(n)]
    global time
    cnt, time = 0, 0

    for u in range(n):
        if discovery[u] is None:
            if BridgeVisit(u, G, discovery, parent, is_art, low) > 1: is_art[u] = True
            else: is_art[u] = False

    for u in range(n):
        if is_art[u]: cnt += 1
        
    return cnt

def BridgeVisit(u:int, G:list, discovery:list, parent:list, is_art:list, low:list) -> None:
    global time
    children = 0

    time += 1
    low[u] = time
    discovery[u] = time

    for v in G[u]:
        if discovery[v] is None:
            children += 1
            BridgeVisit(v, G, discovery, parent, is_art, low)

            if low[v] >= discovery[u]: is_art[u] = True

            low[u] = min(low[u], low[v])
        else:
            low[u] = min(low[u], discovery[v])

    return children

def list_form(B:list) -> list:
    n = 0
    B = preprocess(B)
    for edge in B: n = max(n, edge[0], edge[1])

    G = [[] for _ in range(n + 1)]

    for edge in B:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])

    return G

# nlogn preprocessing
def preprocess(B:list) -> list:
    for i in range(len(B)):
        B[i] = min(B[i]), max(B[i])

    B.sort(key = lambda x : (x[0], x[1]))

    T = []
    prev = None

    for edge in B:
        if edge == prev: continue
        T.append(edge)
        prev = edge
    
    return T

# Adrian Suliga
# Algorytm przepisuje listę połączeń na graf w postaci listy krawędzi przy czym każde
# połączenie jest traktowane jako połączenie w obie strony. Następnie dla każdego wierzchołka
# grafu sprawdzamy czy usunięcie go rozspójni graf. Jeśli tak, to zwiększamy odpowiedni licznik
# Szacuję złożoność czasową algorytmu na O(n + n(n + v)) = O(n^2) gdzie v to ilość wierzchołków, v < n
# złożoność pamięciowa algorytmu to natomiast O(n)

"""def koleje ( B ):
    G = list_form(B)
    n = len(G)
    cnt = 0

    for u in range(n):
        if not is_coherent(G, u): 
            cnt += 1

    return cnt

def is_coherent(G:list, banned:int) -> bool:
    n = len(G)
    visited = [False for _ in range(n)]
    visited[banned] = True

    if banned == 0: DFSVisit(G, 1, visited)
    else: DFSVisit(G, 0, visited)

    for i in range(n):
        if not visited[i]: return False
    return True

def DFSVisit(G, u, visited):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            DFSVisit(G, v, visited)

def list_form(B:list) -> list:
    n = 0
    B = preprocess(B)
    for edge in B: n = max(n, edge[0], edge[1])

    G = [[] for _ in range(n + 1)]

    for edge in B:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])

    return G

# n^2 preprocessing
def preprocess(B:list) -> list:
    for i in range(len(B)):
        if B[i][0] > B[i][1]:
            B[i] = B[i][1], B[i][0]
    
    T = []

    for edge in B:
        if edge in T: continue
        T.append(edge)

    return T"""

runtests ( koleje, all_tests = True )
