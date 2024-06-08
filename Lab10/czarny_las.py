from math import inf
# Dany jest las drzew, ścięcie drzewa i daje nam zysk p[i]
# nie można ścinać dwóch drzew pod rząd, oblicz maksymalny zysk
# f(i) - maksymalny zysk drwala jeśli kończymy na drzewie i
# f(i) = max { f(i - 1), f(i - 2) + p[i] | i > 1 }
# f(0) = p[0]
# f(1) = max { p[0], p[1] }

def black_forest(p:list) -> int:
    return memo_forest(len(p) - 1, p, {})

def memo_forest(i:int, p:list, memo:dict):
    if i in memo: return memo[i]
    if i == 1: return max(p[0], p[1])
    if i == 0: return p[0]

    result = max(memo_forest(i - 1, p, memo), memo_forest(i - 2, p, memo) + p[i])
    memo[i] = result
    return result

def tab_forest(p:list) -> int:
    n = len(p)
    F = [-inf for _ in range(n)]
    F[0] = p[0]
    F[1] = max(p[0], p[1])

    for i in range(2, n):
        F[i] = max(F[i - 1], F[i - 2] + p[i])

    return F[n - 1]