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
        for v in G[u]:
            if cost + 1 < d[v]:
                d[v] = d[u] + 1
                Q.put((d[v], v))

    return d

G = [
    [1, 3],
    [5],
    [],
    [2, 4],
    [],
    []
]

print(shortest_paths(G, 0))