def bridges(G:list) -> list:
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    times = [-1 for _ in range(n)]
    low = [None for _ in range(n)]
    bridge = []
    global time

    time = 0

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u, visited, parent, times, low)

    for i in range(n):
        if parent[i] != None and times[i] == low[i]:
            bridge.append((parent[i], i))

    return bridge

def DFSVisit(G, u, visited, parent, times, low):
    global time
    min_par = float('inf')
    min_ch = float('inf')
    ancs = []
    children = []

    time += 1
    visited[u] = True
    times[u] = time

    for v in G[u]:
        if not visited[v]:
            parent[v] = u
            children.append(v)
            DFSVisit(G, v, visited, parent, times, low)
        elif v != parent[u]: ancs.append(v)
        
    for i in range(len(ancs)):
        min_par = min(min_par, times[ancs[i]])

    for i in range(len(children)):
        min_ch = min(min_ch, low[children[i]])

    low[u] = min(times[u], min_par, min_ch)

G = [
    [1, 2, 3],
    [0, 2],
    [0, 1, 6],
    [0, 4],
    [3, 5],
    [4],
    [2, 7, 8],
    [6, 8],
    [6, 7]
]
print(bridges(G))