def BFS(G, s):
    n = len(G) # n = V

    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)]

    d[s] = 0
    visited[s] = True
    Q = []
    Q.append(s)
    while len(Q) > 0:
        u = Q.pop(0)
        print(u)
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                Q.append(v)
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