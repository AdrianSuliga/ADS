from egz3atesty import runtests
from queue import PriorityQueue
def goodknight( G, s, t ):
    G = list_form(G)
    n = len(G)
    d = [[float('inf') for _ in range(17)] for _ in range(n)]
    Q = PriorityQueue()

    d[s][0] = 0
    Q.put((d[s][0], 0, s)) # [koszt dotarcia do s przy i przejechanych godzinach, ilość przejechanych godzin, wierzchołek]

    while not Q.empty():
        weight, hours, u = Q.get()
        if weight == d[u][hours]:
            for v, cost in G[u]:
                if hours + cost <= 16 and d[u][hours] + cost < d[v][hours + cost]:
                    d[v][hours + cost] = d[u][hours] + cost
                    Q.put((d[v][hours + cost], hours + cost, v))
                elif d[u][hours] + cost + 8 < d[v][cost]:
                    d[v][cost] = d[u][hours] + cost + 8
                    Q.put((d[v][cost], cost, v))

    return min(d[t])

def list_form(G:list) -> list:
    n = len(G)
    R = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if G[u][v] > -1:
                R[u].append((v, G[u][v]))
                
    return R

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )

G  = [ [ -1, 3, 8,-1,-1,-1 ], # 0
[ 3,-1, 3, 6,-1,-1 ], # 1
[ 8, 3,-1,-1, 5,-1 ], # 2
[ -1, 6,-1,-1, 7, 8 ], # 3
[ -1,-1, 5, 7,-1, 8 ], # 4
[ -1,-1,-1, 8, 8,-1 ]]
#print(goodknight(G, 0, 5))