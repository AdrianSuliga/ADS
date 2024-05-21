from kol3btesty import runtests
from queue import PriorityQueue

# Adrian Suliga
# Algorytm dodaje do grafu nowy wierzchołek, nazwijmy go NIEBEM.
# NIEBO łączymy z każdym wierzchołkiem grafu tak aby waga dodawanej krawędzi
# była równa kosztowi wystartowania/wylądowania szybowcem z danego wierzchołka
# Na tak zmodyfikowanym grafie uruchamiany jest algorytm Dijkstry. Do grafu
# maksymalnie dodajemy V krawędzi, zatem złożoność czasową algorytmu szacuję jako 
# O((E + V)log(E + V)), czyli O(ElogV), a pamięciową na O(E + V)

def airports( G, A, s, t ):
    expand_graph(G, A)
    n = len(G)
    d = [float('inf') for _ in range(n)]
    Q = PriorityQueue()

    d[s] = 0
    for u in range(n):
        Q.put((d[u], u))
    
    while not Q.empty():
        _, u = Q.get()
        for v, cost in G[u]:
            if d[u] + cost < d[v]:
                d[v] = d[u] + cost
                Q.put((d[v], v))

    return d[t]

def expand_graph(G:list, A:list) -> None:
    n = len(G)
    G.append([])
    for u in range(n):
        G[u].append((n, A[u]))
        G[n].append((u, A[u]))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )
