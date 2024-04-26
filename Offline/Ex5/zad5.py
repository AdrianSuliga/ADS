from queue import PriorityQueue
from zad5testy import runtests

def spacetravel( n, E, S, a, b ):
    new_vertexes(E, S) # dodanie S^2/2 krawędzi, O(S^2)
    G = list_form(E) # Przepisanie na reprezentację listową O(E + S^2)
    size = len(G)
    
    parent = [None for _ in range(size)]
    distance = [float('inf') for _ in range(size)]
    Q = PriorityQueue()

    distance[a] = 0
    for i in range(size):
        Q.put((distance[i], i))
    
    while not Q.empty(): # Algorytm Dijkstry O((E + S^2)logV) gdzie S może być rzędu V, mamy więc O((E + V^2)logV) przy czym
        _, u = Q.get()  # E < V^2, zatem dostajemy O(V^2logV)
        for v, cost in G[u]:
            if cost + distance[u] < distance[v]:
                distance[v] = cost + distance[u]
                parent[v] = u
                Q.put((distance[v], v))

    if distance[b] == float('inf'): return None
    else: return distance[b]
    

def new_vertexes(E:list, S:list) -> None:
    n = len(S)
    for i in range(n):
        for j in range(i + 1, n):
            E.append((S[i], S[j], 0))

def list_form(E:list) -> list: # O(E + S^2)
    V = size_of_graph(E)
    G = [[] for _ in range(V)]

    for edge in E:
        G[edge[0]].append((edge[1], edge[2]))  
        G[edge[1]].append((edge[0], edge[2]))
    
    return G

def size_of_graph(E:list) -> int: # O(E + S^2)
    result = -1
    for edge in E:
        result = max(result, edge[0], edge[1])
    return result + 1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
"""E=[(0, 1, 5), (1, 2, 21), (1, 3, 1), (2, 4, 7), (3, 4, 13), (3, 5, 16), (4, 6, 4), (5, 6, 1)]
S=[0, 2, 3]
a=1
b=5
print(spacetravel(8, E, S, a, b))"""