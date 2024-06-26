# graf skierowany, znajdź dobry początek o ile istnieje
# dobry początek - wierzchołek, z którego można dojść do każdego innego

def good_start(G:list) -> int: # wierzchołek z najwyższym czasem przetworzenia jest jedynym
    n = len(G)                 # kandydatem na dobry początek, jak on nim nie jest to go nie ma
    visited = [False for _ in range(n)]
    times = [False for _ in range(n)]
    candidate = -1
    global time

    time = -1

    for i in range(n):
        if not visited[i]:
            DFS2Visit(G, i, visited, times)

    for i in range(n):
        if times[i] == n - 1:
            candidate = i
            break
    
    if is_good_start(G, candidate): return candidate
    else: return None
    
def is_good_start(G:list, u:int) -> bool:
    n = len(G)
    visited = [False for _ in range(n)]

    DFSVisit(G, u, visited)

    for i in range(n):
        if not visited[i]: return False
    return True

def DFS2Visit(G:list, u:int, visited:list, times:list):
    visited[u] = True
    global time

    for v in G[u]:
        if not visited[v]:
            DFS2Visit(G, v, visited, times)
    
    time += 1
    times[u] = time

def brute_force(G:list) -> int: # dla każdego wierzchołka sprawdzamy czy jest dobrym początkiem
    n = len(G)                  # za pomocą DFSa. Złożoność czasowa to O(V(E + V)) = O(VE + V^2)
    visited = [False for _ in range(n)]
    is_good_start = True

    for u in range(n):
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

print(good_start(G))