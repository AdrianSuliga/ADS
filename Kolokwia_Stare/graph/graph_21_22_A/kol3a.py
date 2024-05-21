from kol3atesty import runtests
from queue import PriorityQueue
def spacetravel( n, E, S, a, b ):
    add_new_v(E, S, n)
    G = list_form(E, n + 1)
    d = [float('inf') for _ in range(n + 1)]
    Q = PriorityQueue()

    d[a] = 0
    for u in range(n):
        Q.put((d[u], u))

    while not Q.empty():
        _, u = Q.get()
        for v, cost in G[u]:
            if d[u] + cost < d[v]:
                d[v] = d[u] + cost
                Q.put((d[v], v))

    return d[b] if d[b] != float('inf') else None

def add_new_v(E:list, S:list, n:int) -> None:
    for black_hole in S:
        E.append((black_hole, n, 0))

def list_form(E:list, n:int) -> list:
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append((edge[1], edge[2]))
        G[edge[1]].append((edge[0], edge[2]))
    return G

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
