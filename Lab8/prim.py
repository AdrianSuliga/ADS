from queue import PriorityQueue
def MST(G:list, s:int) -> list:
    n = len(G)
    d = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = PriorityQueue()

    d[s] = 0
    for u in range(n):
        Q.put((d[u], u))
    
    while not Q.empty():
        _, u = Q.get()
        for v, weight in G[u]:
            if parent[u] != v and d[v] > weight:
                d[v] = weight
                parent[v] = u
                Q.put((d[v], v))
    
    return parent

G = [
    [(1, 2), (2, 3), (3, 4)],
    [(0, 2), (3, 5), (4, 7)],
    [(0, 3), (3, 2), (5, 1)],
    [(0, 4), (1, 5), (4, 1), (5, 5), (2, 2)],
    [(1, 7), (3, 1), (5, 3)],
    [(2, 1), (3, 5), (4, 3)]
]

print(MST(G, 0))