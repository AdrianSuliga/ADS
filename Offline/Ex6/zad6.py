from zad6testy import runtests
from queue import PriorityQueue

# Adrian Suliga
# Algorytm przepisuje graf na listę krawędzi, następnie dodaje krawędzie dwumilowe, takie które są efektem skoku butami
# dla odróżnienia krawędzie dwumilowe mają postać (wierzchołek, koszt, True), a normallne (wierzchołek, koszt, False).
# Następnie na takim grafie uruchamiany jest zmodyfikowany algorytm Dijkstry, który oblicza optymalny czas dotarcia
# do wierzchołka i jeśli doszło się do niego normalnie (d[i]) lub doskoczyło się do niego (d[i + n]). Szacuję złożoność
# czasową algorytmu na O(V^3), a pamięciową na O(V^2).

def jumper( G, s, w ):
    n = len(G)
    G = list_form(G) # O(V^2)
    G = add_edges(G) # O(V^3)
    d = [float('inf') for _ in range(2 * n)]
    Q = PriorityQueue()

    d[s] = 0
    Q.put((d[s], s, True))

    while not Q.empty(): # O(ElogV) = O(V^2 logV)
        _, u, can_jump = Q.get()

        if can_jump:
            for v, cost, is_jump in G[u]:
                if is_jump and d[u] + cost < d[v + n]: # jeśli skaczemy to zapisujemy w polu v + n
                    d[v + n] = d[u] + cost
                    Q.put((d[v + n], v, False))
                elif not is_jump and d[u] + cost < d[v]: # jeśli nie skaczemy to zapisujemy w polu v
                    d[v] = d[u] + cost
                    Q.put((d[v], v, True))
        else:
            for v, cost, is_jump in G[u]:
                if not is_jump and d[u + n] + cost < d[v]: # jeśli nie możemy skoczyć to nie 
                    d[v] = d[u + n] + cost # możemy brać pod uwagę u tylko u + n
                    Q.put((d[v], v, True))

    return min(d[w], d[w + n])

def add_edges(G:list) -> list:
    n = len(G)

    Gr = [[] for _ in range(n)]

    for u in range(n): # normalne krawędzie, nie skaczemy po
        for v, cost in G[u]: # nich butami
            Gr[u].append((v, cost, False))

    for u in range(n): # krawędzie dwumilowe
        for v, costv in G[u]: # reprezentują skok butami
            for x, costx in G[v]:
                if x != u:
                    Gr[u].append((x, max(costv, costx), True))

    return Gr

def list_form(G:list) -> list:
    n = len(G)
    Gr = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] > 0:
                Gr[i].append((j, G[i][j]))

    return Gr

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )