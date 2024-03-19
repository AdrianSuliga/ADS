from zad3testy import runtests

def dominance(P:list):
    n = len(P)
    max_dominance = -float('inf')
    for i in range(n):
        domi = 0
        for j in range(n):
            if P[i][0] > P[j][0] and P[i][1] > P[j][1]:
                domi += 1
        max_dominance = max(max_dominance, domi)
    return max_dominance
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
