from queue import PriorityQueue
from zad5testy import runtests

# Adrian Suliga
# Algorytm dodaje do grafu jeden wierzchołek, połączony z każdą z osobliwości krawędzią o koszcie 0
# robi to poprzez dodanie S krawędzi (wierzchołek, osobliwość, 0). Następnie graf jest przepisywany na 
# reprezentację listową, na której uruchamiany jest algorytm Dijkstry. Złożoność czasową algorytmu szacuję
# na O((E + V)logV), czyli O(ElogV), natomiast pamięciową na O(E + V) z powodu reprezentacji grafu i tablic pomocniczych

def spacetravel( n, E, S, a, b ):
    new_vertex(E, S) # dodanie S krawędzi
    G = list_form(E) # Przepisanie na reprezentację listową O(E + V)
    size = len(G)
    
    parent = [None for _ in range(size)]
    distance = [float('inf') for _ in range(size)]
    Q = PriorityQueue()

    distance[a] = 0
    for i in range(size):
        Q.put((distance[i], i))
    
    while not Q.empty(): # Algorytm Dijkstry O((E + S)log(E + S)) gdzie S może być rzędu V, mamy więc O((E + V)logV)
        _, u = Q.get()
        for v, cost in G[u]:
            if cost + distance[u] < distance[v]:
                distance[v] = cost + distance[u]
                parent[v] = u
                Q.put((distance[v], v))

    if distance[b] == float('inf'): return None
    else: return distance[b]

def list_form(E:list) -> list: # O(E + S), czyli O(E + V)
    V = size_of_graph(E)
    G = [[] for _ in range(V)]

    for edge in E:
        G[edge[0]].append((edge[1], edge[2]))  
        G[edge[1]].append((edge[0], edge[2]))
    
    return G

def new_vertex(E:list, S:list) -> None: # O(S), czyli O(V) w najgorszym przypadku, dodajemy 1 wierzchołek i max. V krawędzi
    V = size_of_graph(E)
    for vertex in S:
        E.append((V, vertex, 0))

def size_of_graph(E:list) -> int: # O(E + S), czyli O(E + V)
    result = -1
    for edge in E:
        result = max(result, edge[0], edge[1])
    return result + 1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )