# Dana jest szachownica liczb wymmiernych n x n
# chcemy przejść z pola (1, 1) na pole (n, n)
# korzystając jedynie z ruchów: w dół, w prawo
# wejście na pole (i, j) kosztuje A[i][j]

# f(i, j) = min { f(i, j - 1), f(i - 1, j) } + A[i][j]
# f(0, 0) = A[0][0]

def tab_king(M:list) -> int: # O(n^2) czas i pamięć
    n = len(M)
    F = [[float('inf') for _ in range(n)] for _ in range(n)]

    F[0][0] = M[0][0]

    for i in range(n):
        for j in range(n):
            if i == j == 0: continue
            if i > 0: F[i][j] = min(F[i][j], F[i - 1][j])
            if j > 0: F[i][j] = min(F[i][j], F[i][j - 1])
            F[i][j] += M[i][j]

    return F[n - 1][n - 1]

def dyn_king(M:list, i:int, j:int, memo:dict) -> int: # O(n^2) czas i pamięć
    if (i, j) in memo: return memo[(i, j)]
    if i == j == 0: return M[i][j]
    if i < 0 or j < 0: return float('inf')
    
    result = min(dyn_king(M, i - 1, j, memo), dyn_king(M, i, j - 1, memo)) + M[i][j]
    memo[(i, j)] = result
    return result

M = [
    [1, 2],
    [3, 1]
]
n = len(M) - 1

print(dyn_king(M, n, n, {}))
print(tab_king(M))