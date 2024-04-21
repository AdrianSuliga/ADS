# Graf nieskierowany, reprezentowany przez macierz sąsiedztwa
def cycle_4(G:list) -> bool: # O(n^4) brute force
    n = len(G)
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for m in range(k + 1, n):
                    if G[i][j] and G[j][m] and G[m][k] and G[k][i]: return True
                    elif G[i][m] and G[i][j] and G[k][m] and G[k][j]: return True
                    elif G[i][k] and G[i][m] and G[m][j] and G[k][j]: return True
    return False

def cycle_4_opt(G:list) -> bool: # O(n^3) optimized
    n = len(G)
    for i in range(n - 1):
        for j in range(i + 1, n):
            cnt = 2
            for k in range(n):
                if G[i][k] and G[j][k]: cnt += 1
                if cnt >= 4: return True
    return False

G = [
    [0, 0, 1, 0, 0, 0, 0], # i
    [0, 0, 1, 1, 1, 0, 1], # j
    [1, 1, 0, 1, 0, 0, 0], # k
    [0, 1, 1, 0, 1, 0, 0], # m
    [0, 1, 0, 1, 0, 1, 0], #
    [0, 0, 0, 0, 1, 0, 0], #
    [0, 1, 0, 1, 0, 0, 0]  #
]
print(cycle_4_opt(G))