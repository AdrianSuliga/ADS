from queue import PriorityQueue
# graf przedstawia stację benzynową wraz z kosztami dojazdu do nich w litrach paliwa 
# D - pojemność baku pojazdu, C[] - koszt dojazdu
# napisz algorytm obliczający optymalny koszt dojazdu z s do e
# złożoność docelowa: O(DE * log(DV))

def gas_station(G:list, C:list, Max_Fuel:int, Current_Fuel:int, start:int, end:int) -> int:
    cost = dijkstra_modified(G, C, Max_Fuel, Current_Fuel, start, end)
    return min(cost[end])

def dijkstra_modified(G:list, C:list, Max_Fuel:int, Current_Fuel:int, start:int, end:int) -> list:
    n = len(G)
    cost = [[float('inf') for _ in range(Max_Fuel + 1)] for _ in range(n)] # koszt dodarcia do wierzchołka 
    # i (0 <= i <= n) przy ilości paliwa j (0 <= j <= Max_Fuel)
    Q = PriorityQueue()
    cost[start][Current_Fuel] = 0

    Q.put((cost[start][Current_Fuel], Current_Fuel, start))

    while not Q.empty():
        _, Amount_of_Fuel, u = Q.get()
        for v, length in G[u]:
            for d in range(Max_Fuel - Amount_of_Fuel + 1):
                if length <= d + Amount_of_Fuel and cost[u][Amount_of_Fuel] + d * C[u] < cost[v][Amount_of_Fuel + d - length]:
                    cost[v][Amount_of_Fuel + d - length] = cost[u][Amount_of_Fuel] + d * C[u]
                    Q.put((cost[u][Amount_of_Fuel] + d * C[u], d + Amount_of_Fuel - length, v))
                    
    return cost

def create_graph(E:list) -> list:
    n = 0
    for edge in E:
        n = max(edge[0], edge[1], n)

    G = [[] for _ in range(n + 1)]

    for edge in E:
        G[edge[0]].append((edge[1], edge[2]))
        G[edge[1]].append((edge[0], edge[2]))

    return G

E = [(0, 1, 4), (0, 7, 5), (0, 6, 8), (6, 7, 3), (1, 6, 6), (7, 8, 20), (8, 4, 9),
     (5, 6, 12), (5, 4, 7), (1, 2, 15), (5, 2, 17), (2, 4, 10), (2, 3, 5), (4, 3, 18)]
C = [5, 7, 3, 5, 2, 1, 8, 10, 6]
s = 0
e = 3
D = 14
fuel = 5

print(gas_station(create_graph(E), C, D, fuel, s, e))