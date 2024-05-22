from queue import PriorityQueue
def gas_station(G:list, Cost:list, MaxFuel:int, InitialFuel:int, Start:int, End:int) -> int:
    n = len(G)
    d = [[float('inf') for _ in range(MaxFuel + 1)] for _ in range(n)]
    Q = PriorityQueue()

    d[Start][InitialFuel] = 0
    Q.put((d[Start][InitialFuel], InitialFuel, Start))

    while not Q.empty():
        _, CurrentFuel, Vertex = Q.get()
        for Neighbour, Weight in G[Vertex]:
            for BoughtFuel in range(MaxFuel - CurrentFuel + 1):
                if Weight <= BoughtFuel + CurrentFuel and d[Vertex][CurrentFuel] + BoughtFuel * Cost[Vertex] < d[Neighbour][CurrentFuel + BoughtFuel - Weight]:
                    d[Neighbour][CurrentFuel + BoughtFuel - Weight] = d[Vertex][CurrentFuel] + BoughtFuel * Cost[Vertex]
                    Q.put((d[Neighbour][CurrentFuel + BoughtFuel - Weight], CurrentFuel + BoughtFuel - Weight, Neighbour))

    return min(d[End])

def create_graph(E:list) -> list:
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
s = 0
e = 4
D = 10
fuel = 0

print(gas_station(create_graph(E), C, D, fuel, s, e))