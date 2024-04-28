# graf skierowany, znajdź dobry początek o ile istnieje
# dobry początek - wierzchołek, z którego można dojść do każdego innego

def brute_force(G:list) -> int: # dla każdego wierzchołka sprawdzamy czy jest dobrym początkiem
    n = len(G)                  # za pomocą DFSa. Złożoność czasowa to O(V(E + V)) = O(VE + V^2)
    visited = [False for _ in range(n)]
    is_good_start = True

    for u in range(n):
        visited[u] = True
        DFSVisit(G, u, visited)
        for i in range(n):
            if not visited[i]:
                is_good_start = False
                break
        if is_good_start: return u
        is_good_start = True
        visited = [False for _ in range(n)]
    return None

def DFSVisit(G:list, u:int, visited:list) -> None:
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            DFSVisit(G, v, visited)

G = [
    [],
    [0, 3],
    [1],
    [],
    [2, 3, 5],
    [6],
    []
]
print(brute_force(G))