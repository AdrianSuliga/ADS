from queue import PriorityQueue
def travel_plan(G:list, s:int, e:int) -> list:
    len_1, path_1 = dijkstra_modified(G, s, e, "A") # Bob pojedzie pierwszy
    len_2, path_2 = dijkstra_modified(G, s, e, "B") # Alice pojedzie pierwsza
    if len_1 < len_2: return "BOB", path_1 
    else: return "ALICE", path_2

def dijkstra_modified(G:list, s:int, e:int, who:str) -> tuple:
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = PriorityQueue()

    distance[s] = 0
    Q.put((distance[s], s, who))

    while not Q.empty():
        _, u, prev_driver = Q.get()
        for v, weight in G[u]:
            if not visited[v]:
                if prev_driver == "A":
                    distance[v] = distance[u]
                    parent[v] = u
                    Q.put((distance[v], v, "B"))
                elif prev_driver == "B":
                    if distance[u] + weight < distance[v]:
                        distance[v] = distance[u] + weight
                        parent[v] = u
                        Q.put((distance[v], v, "A"))

        visited[u] = True

        if u == e:
            result, buffer = [e], parent[e]
            while buffer != None and buffer != s:
                result.append(buffer)
                buffer = parent[buffer]
            result.append(s)
            result.reverse()
            return distance[e], result
    
    result, buffer = [e], parent[e]
    while buffer != None and buffer != s:
        result.append(buffer)
        buffer = parent[buffer]
    result.append(s)
    result.reverse()
    return float('inf'), result

G = [
    [(1, 50), (2, 40), (3, 80)],
    [(0, 50), (3, 60)],
    [(0, 40), (5, 30)],
    [(0, 80), (1, 60), (4, 20)],
    [(3, 20), (5, 70), (6, 80)],
    [(2, 30), (4, 70), (6, 30), (5, 90)],
    [(4, 80), (5, 30), (7, 40)],
    []
]

print(travel_plan(G, 0, 7))