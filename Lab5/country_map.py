# dana jest mapa kraju, którego drogi objęte są opłatami 0 lub 1
# znajdź najtańszą drogę z x do y
# jedną opcją jest algorytm Dijkstry o złożoności ElogV, można jednak szybciej
# uruchamiamy BFS, ale kolejka priorytetyzuje wierzchołki, do których
# możemy dojść w 0
from queue import Queue
from queue import PriorityQueue
def cheapest_path(G:list, x:int, y:int) -> list: # O(E + V)
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    Q0 = Queue()
    Q1 = Queue()

    visited[x] = True
    Q1.put((x, None))

    while not Q1.empty() or not Q0.empty():
        if not Q0.empty(): u, par_u = Q0.get()
        else: u, par_u = Q1.get()

        visited[u] = True
        if parent[u] == None: parent[u] = par_u

        for v, cost in G[u]:
            if not visited[v]:
                if cost == 0: Q0.put((v, u))
                else: Q1.put((v, u))

    result = []
    result.append(y)
    buffor = parent[y]
    while buffor != x and buffor != None:
        result.append(buffor)
        buffor = parent[buffor]
    result.append(x)
    reverse(result)
    return result

def reverse(T:list) -> None:
    i, j = 0, len(T) - 1
    while i < j:
        T[i], T[j] = T[j], T[i]
        i += 1
        j -= 1

def Dijkstra_algorithm(G:list, x:int, y:int) -> int: # O(ElogV)
    n = len(G)
    d = [float('inf') for _ in range(n)]
    parent = [float('inf') for _ in range(n)]
    Q = PriorityQueue()

    d[x] = 0
    for i in range(n):
        Q.put((d[i], i))
    
    while not Q.empty():
        _, u = Q.get()
        for v, cost in G[u]:
            if d[u] + cost < d[v]:
                d[v] = d[u] + cost
                parent[v] = u
                Q.put((d[v], v))

    result = []
    result.append(y)
    buffor = parent[y]
    while buffor != x and buffor != None:
        result.append(buffor)
        buffor = parent[buffor]
    result.append(x)
    reverse(result)
    return result        

G = [
    [(1, 0), (4, 0)],
    [(0, 0), (2, 1), (5, 0)],
    [(1, 1), (3, 0)],
    [(2, 0), (6, 1), (8, 0)],
    [(0, 0), (5, 1)],
    [(4, 1), (1, 0), (6, 1)],
    [(5, 1), (3, 1), (7, 0)],
    [(6, 0), (8, 1)],
    [(3, 0), (7, 1)]
]
print(cheapest_path(G, 0, 8))
print(Dijkstra_algorithm(G, 0, 8))