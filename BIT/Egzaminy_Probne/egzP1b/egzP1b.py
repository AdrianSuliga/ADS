from egzP1btesty import runtests 
from queue import PriorityQueue
from math import inf

# Adrian Suliga
# Algorytm oblicza optymalny czas dotarcia z D do każdego wierzchołka jeśli wcześniej byliśmy w 0, 1, 2, 3 lub 4 wierzchołkach i zapisuje go do tablicy d[][].
# W treści zadania jest napisane, że wierzchołka początkowego nie liczymy jako punktu turystycznego i musimy odwiedzić 3 punkty turystyczne. Algorytm uznaje 
# D jako punkt turystyczny, więc wynikiem jest d[L][4]. Szacuję złożoność czasową algorytmu jako O(ElogV), a pamięciową jako O(E + V)

def turysta( G, D, L ):
    n = len(G)
    G = list_form(G)
    d = [[inf for _ in range(5)] for _ in range(n)] # d[i][j] - minimalna odległość dotarcia do i. wierzchołka jeśli wcześniej odwiedziliśmy j wierzchołków
    Q = PriorityQueue()

    d[D][0] = 0
    Q.put((d[D][0], D, 0))

    while not Q.empty():
        _, Vertex, Counter = Q.get()
        if Counter < 4:
            for Neighbour, Cost in G[Vertex]:
                if d[Vertex][Counter] + Cost < d[Neighbour][Counter + 1]:
                    d[Neighbour][Counter + 1] = d[Vertex][Counter] + Cost
                    Q.put((d[Neighbour][Counter + 1], Neighbour, Counter + 1))

    return d[L][4]

def list_form(G):
    size = 0
    for edge in G:
        size = max(edge[0], edge[1])
    size += 1

    Gr = [[] for _ in range(size)]

    for edge in G:
        Gr[edge[0]].append((edge[1], edge[2]))
        Gr[edge[1]].append((edge[0], edge[2]))

    return Gr

runtests ( turysta )