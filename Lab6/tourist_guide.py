from queue import Queue
from math import ceil
def tourist_guide(G:list, K:int, s:int, e:int) -> int:
    n = len(G)
    Q = Queue()
    parent = [None for _ in range(n)]
    d = [0 for _ in range(n)]

    d[s] = K
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v, load in G[u]:
            weight = min(load, d[u])
            if weight > d[v]:
                parent[v] = u
                d[v] = weight
                Q.put(v)
    
    return ceil(K / d[e])

G = [
    [(1, 20), (2, 30)],
    [(0, 20), (2, 30), (3, 25)],
    [(0, 30), (1, 30), (4, 10), (5, 30)],
    [(1, 25), (4, 20)],
    [(2, 10), (3, 20), (5, 20)],
    [(2, 30), (4, 20)]
]

print(tourist_guide(G, 50, 0, 4))