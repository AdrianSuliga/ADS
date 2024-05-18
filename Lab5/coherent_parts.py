# ile graf ma spójnych składowych?
# dfs dopóki pozostają nieodwiedzone wierzchołki

# Algorytym odwiedza każdy wierzchołek reprezentowanego listą list grafów za pomocą algrytmu DFS, złożoność czasowa to zatem O(V + E) a pamięciowa O(V)

def count_coherent_parts(G):
    def DFS_visit(G, u, visited):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_visit(G, v, visited)

    n = len(G)
    visited = [False for _ in range(n)]
    cnt = 0

    for u in range(n): # iterujemy przez wierzchołki
        if not visited[u]: # jeśli jakiś nie jest odwiedzony to znaleźliśmy nową spójną składową
            cnt += 1
            DFS_visit(G, u, visited) # odwiedzamy wszystkie wierzchołki w owej składowej

    return cnt

G = [
    [3],
    [2, 3],
    [1, 3, 5],
    [0, 1, 2],
    [5],
    [4, 2, 8],
    [7, 8],
    [6, 8],
    [6, 7, 5]
]
print(count_coherent_parts(G))