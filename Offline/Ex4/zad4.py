from zad4testy import runtests

# Adrian Suliga
# Algorytm przepisuje dany graf do postaci list sąsiedztwa w O(V + E), następnie wykorzystuje algorytm DFS do próby odwiedzenia
# wierzchołka y zaczynając za każdym razem z innej krawędzi połączonej z x. Złożoność DFS to O(V + E), w najgorszym przypadku ilość
# krawędzi połączonych z x jest rzędu V, zatem złożoność pamięciowa tej części programu to O(V(V+E) + V + V + V + E) = O(V^2 + VE). 
# Złożoność pamięciowa to natomiast O(V + E + V + V) = O(V + E)

def Flight(L, x, y, t):
    G = rewrite_to_lists(L) 
    V = len(G)
    visited = [False for _ in range(V)] # tablica odwiedzonych wierzchołków i krotek, krotka d[i] opisuje przedział z jakiego może być pułap na jakim wlatujemy do  
    d = [(0, float('inf')) for _ in range(V)] # wierzchołka i. jeśli zaczynaliśmy podróż z wierzchołka x.
    for u in G[x]: 
        if DFSvisit(G, x, u[0], u[1], visited, d, y, t):
            return True
    return False

def DFSvisit(G:list, parent:int, v:int, cost:int, visited:list, d:list, y:int, t:int) -> bool:
    visited[v] = True
    d[v] = common_part(d[parent], (cost - t, cost + t))

    if d[v] == None: # jeśli nie można dolecieć do danego wierzchołka to odznaczamy wszystko i wracamy
        d[v] = (0, float('inf'))
        visited[v] = False
        return False
    
    if v == y: return True # jeśli d[v] != None i dotarliśmy do y, to kończymy algorytm

    for u in G[v]: # odwiedzamy wszystkie możliwe wierzchołki z v
        if not visited[u[0]]:
            if DFSvisit(G, v, u[0], u[1], visited, d, y, t):
                return True
    
    # jeśli nie można nigdzie iść to odznaczamy v i wracamy
    d[v] = (0, float('inf'))
    visited[v] = False
    return False

def common_part(t1:tuple, t2:tuple) -> tuple: # policz część wspólną 2 przedziałów
    if t1[0] > t2[1] or t1[1] < t2[0]: return None
    return (max(t1[0], t2[0]), min(t1[1], t2[1]))

def rewrite_to_lists(L:list) -> list: # przepisz dany graf na postać listową
    V = size_of_graph(L)
    G = [[] for _ in range(V)]
    for edge in L:
        G[edge[0]].append((edge[1], edge[2]))
        G[edge[1]].append((edge[0], edge[2]))
    return G

def size_of_graph(L:list) -> int: # policz ilość wierzchołków
    result = -1
    for edge in L:
        result = max(edge[0], edge[1], result)
    return result + 1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )