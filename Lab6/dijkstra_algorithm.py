from queue import PriorityQueue
def shortest_path(G:list, s:int, e:int) -> list:
    n = len(G)
    parent = [None for _ in range(n)]
    d = [float('inf') for _ in range(n)]
    Q = PriorityQueue() # Priority Queue, pierwsze pole to priorytet, drugie to wartość

    for i in range(n): # defaultowo priority queue przechowuje na początku elementy z min priorytetem
        Q.put((float('inf'), i))
    d[s] = 0

    while not Q.empty():
        _, u = Q.get()
        for v in G[u]:
            if v[1] + d[u] < d[v[0]]:
                d[v[0]] = v[1] + d[u]
                parent[v[0]] = u
                Q.put((d[v[0]], v[0]))
    result = []
    result.append(e)
    buffor = parent[e]
    while buffor != s:
        result.append(buffor)
        buffor = parent[buffor]
    result.append(s)
    return result

G = [
    [(1, 2), (2, 4)], # a 0
    [(0, 2), (2, 1), (3, 4)], # b 1
    [(0, 4), (1, 1), (3, 2), (4, 1)], # c 2
    [(1, 4), (2, 2), (5, 1)], # d 3
    [(2, 1), (5, 3)], # e 4
    [(3, 1), (4, 3)]  # f 5
]
print(shortest_path(G, 0, 5))