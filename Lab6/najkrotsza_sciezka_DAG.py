# znajdź najkrótsze ścieżki w DAGu od danego wierzchołka
from queue import PriorityQueue
def shortest_paths(G:list, source:int) -> list: # brute force, algorytm Dijkstry O(ElogV)
    n = len(G)
    d = [float('inf') for _ in range(n)]
    Q = PriorityQueue()

    d[source] = 0
    for u in range(n):
        Q.put((d[u], u))

    while not Q.empty():
        cost, u = Q.get()
        for v, cost in G[u]:
            if d[u] + cost < d[v]:
                d[v] = d[u] + cost
                Q.put((d[v], v))

    return d

def topologic_sort(G:list) -> list:
    n = len(G)
    visited = [False for _ in range(n)]
    result = []
    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u, visited, result)
            result.append(u)
    return result[::-1]

def shortest(G:list, u:int) -> list:
    V = topologic_sort(G)
    n = len(G)
    d = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    d[u] = 0

    for u in V:
        for v, cost in G[u]:
            if d[u] + cost < d[v]:
                d[v] = d[u] + cost
                parent[v] = u
    
    return d

def DFSVisit(G:list, u:int, visited:list, result:list) -> None:
    visited[u] = True
    for v, _ in G[u]:
        if not visited[v]:
            DFSVisit(G, v, visited, result)
            result.append(v)

G = [
    [(1, 2), (2, 3)],
    [(2, -1), (3, -1)],
    [(4, 5)],
    [(5, 2)],
    [(5, -3)],
    [(6, 3), (7, 1)],
    [],
    []
]

print(shortest(G, 0))