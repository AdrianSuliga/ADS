from kol2testy import runtests
from queue import Queue

# Adrian Suliga
# Algorytm tworzy z grafu listę krawędzi, sortuje je w O(ElogV), następnie
# przesuwa się po liście oknem o rozpiętości V-1 i dla wszystkich krawędzi
# w oknie sprawdza czy tworzony przez nie graf jest spójny i acykliczny czyli
# czy jest drzewem. Złożoność czasową algorytmu szacuję na O(VE), a pamięciową na O(E + V)

def beautree(G):
    n = len(G)
    E = edge_extract(G) # O(E)
    E.sort(key = lambda x: x[2]) # O(ElogV)

    start, end = 0, n - 2
    while end < len(E): # O(E)
        P = E[start : end + 1] 
        if is_tree(P): # O(V)
            sum = 0
            for i in range(start, end + 1): sum += E[i][2] # O(V)
            return sum
        start += 1
        end += 1

    return None

def edge_extract(G:list) -> list:
    E, n = [], len(G)
    for u in range(n):
        for v, w in G[u]:
            if u < v: E.append((u, v, w))
    return E

def list_form(G:list) -> list:
    R = [[] for _ in range(size_of_graph(G))]
    for edge in G:
        R[edge[0]].append((edge[1], edge[2]))
        R[edge[1]].append((edge[0], edge[2]))
    return R

def size_of_graph(G:list) -> int:
    result = 0
    for edge in G:
        result = max(result, edge[0], edge[1])
    return result + 1

def is_tree(G:list) -> bool: # drzewo jest spójne i acykliczne
    G = list_form(G)
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = Queue()

    Q.put(0)

    while not Q.empty():
        u = Q.get()
        visited[u] = True
        for v, _ in G[u]:
            if visited[v] and parent[u] != v: return False
            elif not visited[v]:
                parent[v] = u
                Q.put(v)

    for u in range(n):
        if not visited[u]: return False
    
    return True


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
