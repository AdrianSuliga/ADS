def DFS(G):
    def DFSVisit(G, u, visited):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v, visited)
                print(v, end=' ')

    n = len(G)
    visited = [False for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u, visited)
            print(u, end=' ')
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

DFS(G)