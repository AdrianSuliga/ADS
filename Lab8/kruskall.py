def MST(G:list) -> list:
    n = len(G)
    E = edge_extract(G) # O(E)
    E.sort(key = lambda x: x[2]) # O(ElogE) czyli O(ElogV)
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)] 
    A = []

    for edge in E: # O(E)
        if find(edge[0], parent) != find(edge[1], parent):
            union(edge[0], edge[1], parent, rank)
            A.append(edge)

    return A

def edge_extract(G:list) -> list:
    n = len(G)
    R = []
    for u in range(n):
        for v, cost in G[u]:
            if v >= u: R.append((u, v, cost))
    return R

def find(x:int, parent:list) -> int:
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x:int, y:int, parent:list, rank:list) -> None:
    x = find(x, parent)
    y = find(y, parent)
    if x == y: return
    if rank[x] > rank[y]: parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]: rank[y] += 1

G = [
    [(1, 2), (2, 3), (3, 4)],
    [(0, 2), (3, 5), (4, 7)],
    [(0, 3), (3, 2), (5, 1)],
    [(0, 4), (1, 5), (4, 1), (5, 5), (2, 2)],
    [(1, 7), (3, 1), (5, 3)],
    [(2, 1), (3, 5), (4, 3)]
]

print(MST(G))