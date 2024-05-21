from egz3atesty import runtests
from queue import PriorityQueue
def goodknight( G, s, t ):
    G = list_form(G)
    n = len(G)
    d = [[float('inf') for _ in range(17)] for _ in range(n)]
    Q = PriorityQueue()

    d[s][0] = 0
    Q.put((d[s][0], 0, s)) # optymalny czas dotarcia do s, ilość h od ostatniego spania, wierzchołek

    while not Q.empty():
        _, time, vertex = Q.get()

        for neighbour, cost in G[vertex]:

            if time + cost <= 16 and d[vertex][time] + cost < d[neighbour][time + cost]:
                d[neighbour][time + cost] = d[vertex][time] + cost
                Q.put((d[neighbour][time + cost], time + cost, neighbour))

            if d[vertex][time] + cost + 8 < d[neighbour][cost]:
                d[neighbour][cost] = d[vertex][time] + cost + 8
                Q.put((d[neighbour][cost], cost, neighbour))

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