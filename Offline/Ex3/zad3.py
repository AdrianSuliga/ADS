from zad3testy import runtests

# Adrian Suliga
# Zauważmy, że: jeżeli punkt jest dominowany, to nie może być punktem z maksymalną dominacją, bo punkt go dominujący
# dominuje tyle punktów co on + 1. Program dla każdego punktu (z pominięciem dominowanych) sprawdza ile punktów jest 
# przez niego dominowanych. Jako że mamy zagnieżdżoną pętlę w pętli, to oceniam złożoność czasową algorytmu na O(n^2).

def dominance(P:list):
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
        max_dominance = max(max_dominance, domi)
    return max_dominance

def dominates(P, i, j):
    if P[i][0] > P[j][0] and P[i][1] > P[j][1]:
        return True
    return False

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
