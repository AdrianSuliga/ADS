# find euler cycle in graph
def euler_cycle(G):
    result = []

    DFSVisit(G, 0, G[0][0], result) # O(V + E) to złożoność DFS ale w każdym wywołaniu DFSVisit() używam 
    result.append(0)                # funkcji o złożoności O(V), więc złożoność całości wyniesie nas O(VE + V^2)

    return result                   # złożoność pamięciowa to natomiast O(V + E) ze względu na reprezentację grafu

def DFSVisit(G, u, v, result):
    remove_edge(G, u, v)
    for w in G[v]:
        DFSVisit(G, v, w, result)
    result.append(v)

def remove_edge(G, u, v): # O(V) w najgorszym przypadku - gdy u lub v będą połączone z ilością wierzchołków rzędu V
    u_idx, v_idx = 0, 0
    for i in range(len(G[u])):
        if G[u][i] == v: 
            v_idx = i
            break
    for i in range(len(G[v])):
        if G[v][i] == u:
            u_idx = i 
            break
    G[u][v_idx], G[u][-1] = G[u][-1], G[u][v_idx]
    G[v][u_idx], G[v][-1] = G[v][-1], G[v][u_idx]
    G[u].pop()
    G[v].pop()

def euler_matrix(G): # Złożoność czasowa to O(V^2 + V^2) = O(V^2)
    n = len(G)      # ponieważ przepisujemy graf na reprezentację macierzową, potem na tej reprezentacji
    G_matrix = [[0 for _ in range(n)] for _ in range(n)] # używamy DFS o złożoności O(V^2)

    for i in range(n):
        for j in G[i]:
            G_matrix[i][j] = 1
    
    cycle = []

    visit(G_matrix, 0, cycle)
    return cycle
    
def visit(G, u, cycle):
    n = len(G)
    for i in range(n):
        if G[u][i]:
            G[u][i] = 0
            G[i][u] = 0
            visit(G, i, cycle)
    cycle.append(u)

G = [
    [1, 2],
    [0, 2],
    [0, 1, 3, 4],
    [2, 4, 6, 7],
    [2, 3, 5, 6],
    [4, 6],
    [3, 4, 5, 7],
    [3, 6]
]

print(euler_matrix(G))