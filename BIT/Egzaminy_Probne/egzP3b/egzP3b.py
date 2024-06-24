from egzP3btesty import runtests 
from queue import PriorityQueue

# Adrian Suliga
# Algorytm używa algorytmu Kruskalla do znalezienia makysmalnego drzewa rozpinającego
# grafu G. Jednocześnie aby wypełnić warunek pozostawienia jednego redundantnego połączenia
# podczas przeszukiwania wszystkich krawędzi będziemy sprawdzać (jeśli rozważana krawędź jest redundantna)
# czy nie opłaca nam się jej zawrzeć w ostatecznym wyniku. Szacuję złożoność czasową algorytmu na O(nlogm),
# a pamięciową na O(m + n)

def lufthansa ( G ):
    n, sum, A = len(G), 0, []
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    extra_edge = None
    E = edges(G)

    E.sort(key = lambda x : x[2], reverse = True)

    for edge in E:
        if find(edge[0], parent) != find(edge[1], parent):
            union(edge[0], edge[1], parent, rank)
            A.append(edge)
        elif extra_edge == None or edge[2] > extra_edge[2]:  
            extra_edge = edge
        sum += edge[2]

    result = extra_edge[2]
    for edge in A: result += edge[2]
    return sum - result

# find - union do algorytmu Kruskalla
def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    
    return parent[x]

def union(x, y, parent, rank):
    x = find(x, parent)
    y = find(y, parent)

    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

# zwraca graf w postaci listy krawędzi
def edges(G:list) -> list:
    E = []
    for u in range(len(G)):
        for v, cost in G[u]:
            if v > u:
                E.append((u, v, cost))
    return E

runtests ( lufthansa, all_tests=True )