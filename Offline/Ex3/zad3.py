from zad3testy import runtests

def dominance(P:list):
    n = len(P)
    max_dominance = -float('inf')
    is_dominated = [False for _ in range(n)]

    for i in range(1, n):
        if P[i][0] > P[i - 1][0] and P[i][1] > P[i - 1][1]:
            is_dominated[i - 1] = True
    for i in range(2, n):
        if P[i][0] > P[i - 1][0] and P[i][1] > P[i - 2][1]:
            is_dominated[i - 2] = True

    for i in range(n):
        if is_dominated[i]: continue
        domi = 0
        for j in range(n):
            if P[i][0] > P[j][0] and P[i][1] > P[j][1]:
                domi += 1
                is_dominated[j] = True
        max_dominance = max(max_dominance, domi)
    return max_dominance

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
