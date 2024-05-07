# algorytm floyda-warshalla zwraca macierz 
# gdzie T[i][j] zawiera długość najkrótszej ścieżki
# z i do j
def floyd_warshall(G:list) -> list:
    n = len(G)
    D = [[float('inf') for _ in range(n)] for _ in range(n)]
    
    for u in range(n):
        for v in range(n):
            if u == v: D[u][v] = 0; continue
            if G[u][v] == 0: D[u][v] = float('inf')
            else: D[u][v] = G[u][v]
    for x in range(n):
        for u in range(n):
            for v in range(n):
                D[u][v] = min(D[u][v], D[u][x] + D[x][v])
    
    return D

G = [
    [0, 1, 0, 4, 2, 0],
    [0, 0, 2, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 3, 0, 0],
    [0, 0, 7, 0, 0, 0]
]

min_dist = floyd_warshall(G)
for i in range(len(min_dist)):
    print(min_dist[i])