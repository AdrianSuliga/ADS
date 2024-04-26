from zad3testy import runtests

# Adrian Suliga
# Zauważmy, że: jeżeli punkt jest dominowany, to nie może być punktem z maksymalną dominacją, bo punkt go dominujący
# dominuje tyle punktów co on + 1. Program dla każdego punktu (z pominięciem dominowanych) sprawdza ile punktów jest 
# przez niego dominowanych. Jako że mamy zagnieżdżoną pętlę w pętli, to oceniam złożoność czasową algorytmu na O(n^2).

"""def dominance(P:list): # optimized O(n^2) solution
    n = len(P)
    max_dominance = 0
    is_dominated = [False for _ in range(n)]

    maxDist = 0
    furthestPoint = 0
    for i in range(n): # Dodatkowe usprawnienie, szukamy punktu najbardziej odległego od (0,0) w metryce
        sum = P[i][0] + P[i][1] # manhatańskiej, następnie sprawdzamy które punkty on dominuje. Wyklucza to 
        if sum > maxDist: # sporo punktów z późniejszej pętli n^2
            maxDist = sum
            furthestPoint = i
    for i in range(n):
        if dominates(P, furthestPoint, i):
            is_dominated[i] = True

    for i in range(n):
        if is_dominated[i]: continue
        domi = 0
        for j in range(n):
            if dominates(P, i, j):
                domi += 1
                is_dominated[j] = True
                if domi + n - j < max_dominance: break
        max_dominance = max(max_dominance, domi)
    return max_dominance

def dominates(P, i, j):
    if P[i][0] > P[j][0] and P[i][1] > P[j][1]:
        return True
    return False"""

def dominance(P:list) -> int: # O(n)
    n, max_dominance, fj = len(P), 0, 0
    Y = [0 for _ in range(n + 1)]
    DP = [(0, 0) for _ in range(n + 1)]

    for i in range(n):
        Y[P[i][1]] += 1
    for i in range(n - 1, -1, -1):
        Y[i] += Y[i + 1]
    
    for i in range(n): # DP[i], na prostej x = i znajduje się DP[i][0] punktów, najwyższy ma y-ową współrzędną równą DP[i][1]
        x, y = P[i]
        current = DP[x][0] + 1
        maximum = max(DP[x][1], y)
        DP[x] = (current, maximum)
    for i in range(n, 0, -1):
        domi = n - Y[DP[i][1]] - fj - DP[i][0] + 1
        fj += DP[i][0]
        max_dominance = max(max_dominance, domi)

    return max_dominance    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )