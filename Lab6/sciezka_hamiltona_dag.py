# znajdź ścieżkę hamiltona w DAGu (czy istnieje)
# posortować graf topologicznie, jeśli nie ma połączenia
# między wierzchołkiem i oraz i + 1, to graf nie ma ścieżki
# hamiltona
def hamiltonian_path(G):
    n = len(G)
    visited = [False for _ in range(n)]
    A = []
    def top_sort(G, u):
        visited[u] = True
        for v in G[u]:
            if visited[v] == False:
                top_sort(G, v)
        A.append(u)
    for u in range(n):
        if visited[u] == False:
            top_sort(G, u)
    A.reverse()
    for i in range(n - 1):
        if not A[i + 1] in G[A[i]]:
            return False
    return True

def topologic_sort(G:list) -> bool:
    n = len(G)
    visited = [False for _ in range(n)]
    result = []

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u, visited, result)
            result.append(u)
    
    reverse(result)
    
    for i in range(n - 1):
        if not result[i + 1] in G[result[i]]:
            return False
    return True

def DFSVisit(G:list, u:int, visited:list, result:list) -> None:
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            DFSVisit(G, v, visited, result)
            result.append(v)

def reverse(T:list) -> None:
    i, j = 0, len(T) - 1
    while i < j:
        T[i], T[j] = T[j], T[i]
        i += 1
        j -= 1

G = [
    [1],
    [3],
    [1, 3, 0],
    [4, 5],
    [],
    [4]
]
print(topologic_sort(G))