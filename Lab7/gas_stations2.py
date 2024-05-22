from queue import PriorityQueue
def change_graph(G, C, D):
    n = len(G)
    Gr = [[] for _ in range((D + 1) * n)]

    for u in range(n):
        for v in range(D):
            Gr[u*(D + 1) + v].append((u*(D + 1) + v + 1, C[u]))

    for u in range(n):
        for v, cost in G[u]:
            for x in range(D + 1):
                if x - cost >= 0:
                    Gr[u*(D + 1) + x].append((v*(D + 1) + x - cost, 0))

    return Gr

def dijkstra(G:list, Start:int, End:int, InitialFuel:int, MaxFuel:int) -> list:
    n = len(G)
    d = [float('inf') for _ in range(n)]
    Q = PriorityQueue()
    
    d[Start * (MaxFuel + 1) + InitialFuel] = 0
    Q.put((d[Start * (MaxFuel + 1) + InitialFuel], Start * (MaxFuel + 1) + InitialFuel))

    while not Q.empty():
        _, Vertex = Q.get()
        for Neighbour, Cost in G[Vertex]:
            if d[Vertex] + Cost < d[Neighbour]:
                d[Neighbour] = d[Vertex] + Cost
                Q.put((d[Neighbour], Neighbour))
    
    return min(d[End * (MaxFuel + 1) : End * (MaxFuel + 1) + MaxFuel + 1])

def make_graph(E):
    n = 0
    for edge in E:
        n = max(n, edge[0], edge[1])
    
    G = [[] for _ in range(n + 1)]

    for edge in E:
        G[edge[0]].append((edge[1], edge[2]))
        G[edge[1]].append((edge[0], edge[2]))
    
    return G


E = [(0, 1, 5), (1, 2, 3), (0, 2, 7), (2, 3, 4), (3, 4, 6)]
C = [8, 5, 3, 2, 1]
Start = 0
End = 4
MaxFuel = 10
InitialFuel = 0
G = make_graph(E)
G = change_graph(G, C, MaxFuel)

print(dijkstra(G, Start, End, InitialFuel, MaxFuel))