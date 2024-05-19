# G - nieskierowany, każda krawędź ma wagę
# Czy istnieje ścieżka o malejących wagach?
from queue import Queue
def decreasing_wages(G:list) -> bool: # check if it even exists
    V = len(G) # V

    for x in range(V): # O(V^3 * (V + E))
        for y in range(V):
            if x == y or are_neighbours(G, x, y): continue
            if BFS(G, x, y): return True
    return False

def are_neighbours(G:list, x:int, y:int) -> bool:
    for u in G[x]:
        if y == u[0]: return True
    for u in G[y]:
        if x == u[0]: return True

def BFS(G:list, x:int, y:int) -> bool:
    V = len(G)
    Q = Queue()
    prev = float('inf')
    visited = [False for _ in range(V)]

    visited[x] = True
    Q.put(x)

    while not Q.empty():
        u = Q.get()
        if u == y: return True
        for v in G[u]:
            if not visited[v[0]] and v[1] < prev:
                visited[v[0]] = True
                prev = v[1]
                Q.put(v[0])

    return False

def path_with_dec_wages(G:list, x:int, y:int) -> list[int]: # search for path between x and y
    n = len(G)
    visited = [False for _ in range(n)]
    cost = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    path = []
    Q = Queue()

    visited[x] = True
    cost[x] = float('inf')
    Q.put(x)

    while not Q.empty():
        u = Q.get()
        if u == y:
            path.append(y)
            while parent[y] != x:
                path.append(parent[y])
                y = parent[y]
            path.append(x)
            break
        for v in G[u]:
            if not visited[v[0]] and cost[u] > v[1]:
                visited[v[0]] = True
                parent[v[0]] = u
                cost[v[0]] = v[1]
                Q.put(v[0])
    
    return path

G = [
    [(1, 9), (2, 7)],
    [(0, 9), (2, 11), (4, 12)],
    [(0, 7), (1, 11), (3, 9)],
    [(2, 9), (4, 7)],
    [(1, 12), (3, 7), (5, 6)],
    [(4, 6), (6, 20)],
    [(5, 20)]
]
print(path_with_dec_wages(G, 2, 5))