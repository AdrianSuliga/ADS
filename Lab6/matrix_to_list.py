def matrix_to_list(G:list) -> list:
    n = len(G)
    R = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]:
                R[i].append(j)
    return R

G = [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0]
]
print(matrix_to_list(G))