from math import log2
def minimum_product(G:list, s:int, e:int) -> int:
    n = len(G)
    d = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]

    d[s] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, cost in G[u]:
                if d[u] + log2(cost) < d[v]:
                    d[v] = d[u] + log2(cost)
                    parent[v] = u
    
    for u in range(n):
        for v, cost in G[u]:
            if d[u] + log2(cost) < d[v]: return -float('inf')

    return round(2**(d[e]))

G = [
    [(1, 1), (4, 4)],
    [(0, 1), (2, 3), (4, 1)],
    [(1, 3), (3, 5), (4, 2)],
    [(2, 5), (5, 2)],
    [(0, 4), (1, 1), (2, 2), (5, 10)],
    [(3, 2), (4, 10)]
]

print(minimum_product(G, 0, 2))