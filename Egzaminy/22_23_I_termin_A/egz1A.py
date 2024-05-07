from queue import PriorityQueue
from egz1Atesty import runtests

# Adrian Suliga
# Algorytm oblicza koszt drogi złycerza w każdym z 2V przypadków:
# obrabował 1. zamek, nie obrabował 1. zamku, obrabował 2. zamek, nie obrabował 2. zamku, itd.
# gdy rozważamy obrabowanie i. zamku, to algorytm 

def gold(G, V, s, t, r):
    n = len(G)
    result = float('inf')
    for u in range(n):
        result = min(result, cheapest_path(G, V[u], u, s, t, r))
    result = min(result, standard_dijkstra(G, s, t))
    return result

def standard_dijkstra(G, s, t) -> int:
    n = len(G)
    d = [float('inf') for _ in range(n)]
    Q = PriorityQueue()

    for u in range(n):
        Q.put((d[u], u))
    d[s] = 0

    while not Q.empty():
        _, u = Q.get()
        for v, cost in G[u]:
            if d[u] + cost < d[v]:
                d[v] = d[u] + cost
                Q.put((d[v], v))

    return d[t]

def cheapest_path(P:list, gold, x, s, t, r) -> int:
    n = len(P)
    G = [[] for _ in range(2 * n)]
    for u in range(n):
        for v in P[u]:
            G[u].append(v)
    for i in range(n):
        for j, cost in G[i]:
            G[i + n].append((j + n, 2 * cost + r))

    G[x].append((x + n, 0))
    G[x + n].append((x, 0))

    Q = PriorityQueue()
    d = [float('inf') for _ in range(2 * n)]
    for u in range(n):
        Q.put((d[u], u))
    d[s] = 0

    while not Q.empty():
        _, u = Q.get()
        for v, cost in G[u]:
            if d[u] + cost < d[v]:
                d[v] = d[u] + cost
                Q.put((d[v], v))
 
    return min(d[t], d[t + n] - gold)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
"""G = [
    [(1,9), (2,2)],
    [(0,9), (3,2), (4,6)],
    [(0,2), (3,7), (5,1)],
    [(1,2), (2,7), (4,2), (5,3)],
    [(1,6), (3,2), (6,1)],
    [(2,1), (3,3), (6,8)], 
    [(4,1), (5,8)]
]
V = [25,30,20,15,5,10,0]
print(cheapest_path(G, 30, 1, 0, 6, 7))"""