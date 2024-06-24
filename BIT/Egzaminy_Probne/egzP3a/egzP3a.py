from egzP3atesty import runtests
from math import inf

# Adrian Suliga
# Algorytm m razy oplicza wartości funkcji f takiej że:
# f(i, p) - maksymalna liczba wyborców jaką możemy uzyskać rozważając okręgi do i. oraz mając p pieniędzy
# jest to standardowy algorytm knapsack, zaimplementowany w złożoności O(np) i wywołany m razy
# daje nam złożoność czasową O(mnp) i pamięciową O(np)

class Node:
    def __init__(self, wyborcy, koszt, fundusze):
        self.next = None
        self.wyborcy = wyborcy 
        self.koszt = koszt 
        self.fundusze = fundusze 
        self.x = None

def wybory(T:list[Node]):
    m, result = len(T), 0

    for i in range(m):
        #P = make_list(T[i])
        #result += okrag(P, T[i].fundusze)
        result += f(T[i], T[i].fundusze, {}, 0)
    
    return result

def make_list(node:Node) -> list:
    result = []

    while node != None:
        result.append((node.wyborcy, node.koszt))
        node = node.next

    return result

def okrag(P:list, funds:int) -> int:
    n = len(P)
    F = [[0 for _ in range(funds + 1)] for _ in range(n)]

    for j in range(P[0][1], funds + 1):
        F[0][j] = P[0][0]

    for i in range(1, n):
        for j in range(funds + 1):
            F[i][j] = F[i - 1][j]
            if j >= P[i][1]:
                F[i][j] = max(F[i][j], F[i - 1][j - P[i][1]] + P[i][0])
    
    return F[n - 1][funds]

def f(node:Node, funds:int, memo:dict, i:int):
    if (i, funds) in memo: return memo[(i, funds)]
    if node.next == None and funds < node.koszt: return 0
    if node.next == None and funds >= node.koszt: return node.wyborcy

    result = f(node.next, funds, memo, i + 1)
    if funds >= node.koszt:
        result = max(result, f(node.next, funds - node.koszt, memo, i + 1) + node.wyborcy)

    memo[(i, funds)] = result
    return result

runtests(wybory, all_tests = True)