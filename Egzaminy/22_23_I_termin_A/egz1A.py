from queue import PriorityQueue
from egz1Atesty import runtests

# Adrian Suliga
# Algorytm oblicza koszt drogi złycerza w każdym z 2V przypadków:
# obrabował 1. zamek, nie obrabował 1. zamku, obrabował 2. zamek, nie obrabował 2. zamku, itd.
# gdy rozważamy obrabowanie i. zamku, to algorytm rozszerza graf o jego lustrzane odbicie, ale z krawędziami
# o odpowiednio zwiększonych wagach. Szacuję złożoność algorytmu na O(VElog(VE)), czyli O(V^3 * logV)

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