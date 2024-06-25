from kolutesty import runtests

# Adrian Suliga
# Algorytm zamienia daną listę kolejności zadań na acykliczny, skierowany graf, sortuje go topologicznie,
# a następnie szuka w posortowanym grafie najdłuższej ścieżki za pomocą algorytmu dynamicznego, który
# oblicza wartości funkcji f takiej że:
# f(i) - najdłuższa ścieżka jeśli rozważamy w posortowanym grafie wierzchołki od 0. do i.
# f(i) = max(f(j) + 1 | j to wierzchołek połączony z i)
# f(0) = 1 
# Szacuję złożoność czasową i pamięciową algorytmu na O(m + n)

def projects(n, L):
    G = list_form(n, L)
    S, A = topo_sort(G, n) # S to lista zadań od których należy zacząć, A to wszystkie wierzchołki posortowane topologicznie (po odwróceniu oczywiście)
    A.append(n) # dodajemy sztuczny wierzchołke, który będzie pierwszy w posortowanej tablicy
    A.reverse()
    G.append(S) # do grafu dodajemy sztuczny wierzchołek połączony ze wszystkimi zadaniami, które trzeba wykonać najpierw

    F = [-1 for _ in range(n + 1)] # tablica na wartości funkcji f()
    F[A[0]] = 0 # jest to wartość f dla sztucznego wierzchołka

    for u in A:
        for v in G[u]:
            F[v] = max(F[v], F[u] + 1)

    return max(F)

def topo_sort(G:list, n:int) -> tuple:
    visited = [False for _ in range(n)]
    result, s = [], []

    for u in range(n):
        if not visited[u]:
            DFSVisit(u, G, visited, result)
            result.append(u)

    for u in range(n):
        if not visited[u]:
            s.append(u)

    return s, result

def DFSVisit(u:int, G:list, visited:list, result:list) -> None:
    for v in G[u]:
        if not visited[v]:
            visited[v] = True
            DFSVisit(v, G, visited, result)
            result.append(v)

def list_form(n:int, L:list) -> list:
    G = [[] for _ in range(n)]
    
    for dest, start in L:
        G[start].append(dest)

    return G

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True )