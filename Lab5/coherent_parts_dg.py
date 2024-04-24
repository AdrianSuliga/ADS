def strongly_coherent_parts(G:list) -> list:
    n = len(G)
    visited = [False for _ in range(n)]
    times = [0 for _ in range(n)]
    global time
    time = 0
    for i in range(n):
        if not visited[i]: DFSVisit(G, i, visited, times)
    
    print(times)

def DFSVisit(G:list, u:int, visited:list, times:list) -> None:
    visited[u] = True
    global time
    for v in G[u]:
        if not visited[v]:
            DFSVisit(G, v, visited, times)
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