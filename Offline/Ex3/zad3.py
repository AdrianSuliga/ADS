from zad3testy import runtests

def dominance(P:list):
    n = len(P)
    max_dominance = 0
    is_dominated = [False for _ in range(n)]
    max_point = P[0]

    for i in range(1, n):
        if P[i][1] > max_point[1]:
            max_point = P[i]

    for i in range(n):
        if P[i][0] < max_point[0] and P[i][1] < max_point[1]:
            max_dominance += 1
            is_dominated[i] = True

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
