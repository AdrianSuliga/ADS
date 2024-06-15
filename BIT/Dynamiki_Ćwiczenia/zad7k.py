from zad7ktesty import runtests 

# Adrian Suliga
# Algorytm oblicza najpierw koszt podlania każdego drzewa, następnie uruchamia standardowy
# algorytm knapsack. Szacuję złożoność czasową algorytmu na O(nl), a pamięciową też na O(nl)

def ogrodnik (T, D, Z, l):
    n = len(D)
    C = [0 for _ in range(n)]
    calculate_cost(C, T, D)

    F = [[0 for _ in range(l + 1)] for _ in range(n)]

    for water in range(l):
        if water >= C[0]:
            F[0][water] = Z[0]

    for i in range(1, n):
        for water in range(1, l + 1):
            F[i][water] = F[i - 1][water]
            if water >= C[i] and F[i - 1][water - C[i]] + Z[i] > F[i][water]:
                F[i][water] = F[i - 1][water - C[i]] + Z[i]

    return F[n - 1][l]

def calculate_cost(C:list, T:list, D:list) -> None:
    n = len(D)
    rows, cols = len(T), len(T[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    for i in range(n):
        C[i] = travel(T, 0, D[i], visited)

def travel(T, i, j, visited) -> int:
    visited[i][j] = True
    if T[i][j] == 0: return 0
    result = T[i][j]

    if i + 1 < len(T) and not visited[i + 1][j]:
        result += travel(T, i + 1, j, visited)
    if j + 1 < len(T[0]) and not visited[i][j + 1]:
        result += travel(T, i, j + 1, visited)
    if -1 < j - 1 and not visited[i][j - 1]:
        result += travel(T, i, j - 1, visited)

    return result

# Podejście rekurencyjne, przechodzi 9/10 testów
"""def ogrodnik (T, D, Z, l):
    n = len(D)
    C = [0 for _ in range(n)]
    calculate_cost(C, T, D)
    
    return f(n - 1, Z, C, l, {})

def f(i, Z, C, L, memo):
    if (i, L) in memo: return memo[(i, L)]
    if i == 0 and L < C[i]: return 0
    if i == 0 and L >= C[i]: return Z[i]

    result = f(i - 1, Z, C, L, memo)
    if C[i] <= L:
        result = max(result, f(i - 1, Z, C, L - C[i], memo) + Z[i])

    memo[(i, L)] = result
    return result

def calculate_cost(C:list, T:list, D:list) -> None:
    n = len(D)
    rows, cols = len(T), len(T[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    for i in range(n):
        C[i] = travel(T, 0, D[i], visited)

def travel(T, i, j, visited) -> int:
    visited[i][j] = True
    if T[i][j] == 0: return 0
    result = T[i][j]

    if i + 1 < len(T) and not visited[i + 1][j]:
        result += travel(T, i + 1, j, visited)
    if j + 1 < len(T[0]) and not visited[i][j + 1]:
        result += travel(T, i, j + 1, visited)
    if -1 < j - 1 and not visited[i][j - 1]:
        result += travel(T, i, j - 1, visited)

    return result"""

runtests( ogrodnik, all_tests=True )
