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

def cheapest_path(G, gold, u, s, t, r):
    n = len(G)
    


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
