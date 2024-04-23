# sort topologically DAG - Directed, Acyclic Graph
def topologic_sort(G): # O(2V + E) = O(V + E)
    V = len(G)
    visited = [False for _ in range(V)]
    result = []

    for u in range(V): # O(V + E) - standardowy DFS
        if not visited[u]:
            DFSVisit(G, u, visited, result)
            result.append(u)
    
    return reverse(result) # O(V) na odwrócenie listy

def reverse(result):
    i, j = 0, len(result) - 1
    while i < j:
        result[i], result[j] = result[j], result[i]
        i += 1
        j -= 1
    return result

def DFSVisit(G, u, visited, result):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            DFSVisit(G, v, visited, result)
            result.append(v)

G = [
    [1, 2, 3],
    [5],
    [6],
    [2, 4],
    [],
    [3],
    []
]

print(topologic_sort(G))