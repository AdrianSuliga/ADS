def strongly_coherent_parts(G:list) -> list:
    n = len(G)
    visited = [False for _ in range(n)]
    times = [0 for _ in range(n)]
    global time
    time = 0

    for i in range(n):
        if not visited[i]: DFSVisit(G, i, visited, times)

    T = [0 for _ in range(n)] # w komórce i. przechowujemy kolejność odwiedzania wierzchołka i bazując na czasie odwiedzania z poprzedniego DFSa
    for i in range(n): # komórka z najstarszym czasem odwiedzenia - n, otrzyma numer 0, a z najmniejszym - n - 1
        T[n - times[i]] = i # biorę wierzchołek i, sprawdzam który był odwiedzony w pierwszym DFSie, następnie odwracam tą kolejność za pomocę n - times[i]

    visited = [False for _ in range(n)]
    parts, k = [], 0

    GR = [[] for _ in range(n)] # transpozycja grafu
    for i in range(n):
        for j in range(len(G[i])):
            GR[G[i][j]].append(i)

    for i in range(n): # odwiedzaj transponowany graf dopisując do listy wierzchołki
        if not visited[T[i]]:
            parts.append([])
            SndVisit(GR, T[i], visited, parts[k])
            k += 1

    return parts

def SndVisit(GR:list, u:int, visited:list, parts:list):
    visited[u] = True
    parts.append(u)
    for v in GR[u]:
        if not visited[v]:
            SndVisit(GR, v, visited, parts)

def DFSVisit(G:list, u:int, visited:list, times:list) -> None:
    visited[u] = True

    for v in G[u]:
        if not visited[v]:
            DFSVisit(G, v, visited, times)

    global time
    time += 1
    times[u] = time

G = [
    [1, 7], # a 0
    [2], # b 1
    [0, 3], # c 2
    [6], # d 3
    [3, 9], # e 4
    [4, 8], # f 5
    [5], # g 6
    [8], # h 7
    [9], # i 8
    [7, 10], # j 9
    [8] # k 10
]

print(strongly_coherent_parts(G))