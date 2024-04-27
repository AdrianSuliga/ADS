# szachownica z kosztami przejścia {1, 2, 3, 4, 5}
from queue import Queue
def cheapest_path(G:list) -> int:
    n = len(G)
    visited = [[False for _ in range(n)] for _ in range(n)]
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    Q = Queue()

    Q.put((0, 0, G[0][0]))
    distance[0][0] = 0
    visited[0][0] = True

    while not Q.empty():
        i, j, cost = Q.get()
        if i == j == n - 1:
            return distance[i][j] + cost
        distance[i][j] += 1
        if cost > 1: Q.put((i, j, cost - 1))
        else:
            if i + 1 < n and not visited[i + 1][j]:
                Q.put((i + 1, j, G[i + 1][j]))
                distance[i + 1][j] = distance[i][j]
                visited[i + 1][j] = True
            if i - 1 > -1 and not visited[i - 1][j]:
                Q.put((i - 1, j, G[i - 1][j]))
                distance[i - 1][j] = distance[i][j]
                visited[i - 1][j] = True
            if j + 1 < n and not visited[i][j + 1]:
                Q.put((i, j + 1, G[i][j + 1]))
                distance[i][j + 1] = distance[i][j]
                visited[i][j + 1] = True
            if j - 1 > -1 and not visited[i][j - 1]:
                Q.put((i, j - 1, G[i][j - 1]))
                distance[i][j - 1] = distance[i][j]
                visited[i][j - 1] = True
    for i in range(n):
        print(distance[i])

G = [
    [2, 1, 1, 3],
    [2, 4, 5, 2],
    [1, 3, 5, 1],
    [1, 2, 1, 3]
]
print(cheapest_path(G))