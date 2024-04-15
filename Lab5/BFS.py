from queue import Queue
def BFS(G, u):
    n = len(G)
    Q = Queue()
    d = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    visited[u] = True
    parent[u] = None
    d[u] = -1

    Q.put(u)
    while not Q.empty():
        v = Q.get()
        print(v, end = ' ')
        for p in G[v]:
            if not visited[p]:
                visited[p] = True
                parent[p] = v
                d[p] = d[v] + 1
                Q.put(p)
    print()
                
G = [
    [4],
    [3, 4, 6],
    [3, 4],
    [1, 2],
    [0, 1, 2, 5, 6],
    [4],
    [1, 4]
]
BFS(G, 0)