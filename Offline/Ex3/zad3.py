from zad3testy import runtests

def dominance(P):
    n = len(P)
    dominant = P[0]
    for i in range(1, n):
        x = P[i][0]
        y = P[i][1]
        if min(x, y) > min(dominant[0], dominant[1]) or (min(x, y) == min(dominant[0], dominant[1]) and max(x,y) > max(dominant[0], dominant[1])):
            dominant = P[i]
    result = 0
    for i in range(n):
        if P[i][0] < dominant[0] and P[i][1] < dominant[1]:
            result += 1
    return result
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
