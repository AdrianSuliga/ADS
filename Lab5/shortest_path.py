from queue import Queue
def shortest_path(G:list, x:int, y:int) -> list: # możemy użyć zwykłego BFSa, do wierzchołków w ,,fali" dochodzimy najkrótszymi
    if x == y: return [x]                       # możliwymi ścieżkami
    n = len(G)
    parent = [None for _ in range(n)]
    #d = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    Q = Queue()

    visited[x] = True
    Q.put(x)

    while not Q.empty():
        u = Q.get()
        if u == y: break
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                Q.put(v)

    result = []
    result.append(y)
    buffor = parent[y]
    while buffor != x and buffor != None:
        result.append(buffor)
        buffor = parent[buffor]
    result.append(x)
    return reverse(result)

def reverse(result:list) -> list:
    i, j = 0, len(result) - 1
    while i < j:
        result[i], result[j] = result[j], result[i]
        i += 1
        j -= 1
    return result

G = [
    [1, 2],
    [0, 7],
    [0, 3, 6],
    [2, 4],
    [3, 5, 6],
    [4, 6, 8],
    [2, 4, 5, 7, 8],
    [1, 6],
    [6, 5]
]
print(shortest_path(G, 0, 0))