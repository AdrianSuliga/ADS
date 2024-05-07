from queue import PriorityQueue
from egz1Atesty import runtests

def gold(G,V,s,t,r):
    n = len(G)
    result = float('inf')
    for u in range(n):
        result = min(result, cheapest_path(G, V[u], u, s, t, r))
    result = min(result, standard_dijkstra(G, s, t))
    return result

def standard_dijkstra(G, s, t):
    n = len(G)
    d = [float('inf') for _ in range(n)]
    Q = PriorityQueue()

    d[s] = 0
    for u in range(n):
        Q.put((d[u], u))

    while not Q.empty():
        _, u = Q.get()
        for v, cost in G[u]:
            if d[u] + cost < d[v]:
                d[v] = d[u] + cost
                Q.put((d[v], v))

    return d[t]

def cheapest_path(G:list, gold, u, s, t, r):
    n = len(G)
    for i in range(n):
        G.append([])
    for i in range(n):
        for j in G[i]:
            G[i + n].append((G[i][j][0] + n, 2 * G[i][j][1] + r))
    G[u].append((u + n, 0))
    G[u + n].append((u, 0))
    return gold - min(standard_dijkstra(G, s, t), standard_dijkstra(G, s, t + n))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = False )
