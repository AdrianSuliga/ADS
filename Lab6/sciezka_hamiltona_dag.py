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

G = [
    [1],
    [2, 4],
    [3],
    [4],
    []
]
print(hamiltonian_path(G))