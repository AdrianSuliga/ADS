from egz1btesty import runtests

# Adrian Suliga
# Algorytm na potrzeby obliczania funkcji f(i, b) tworzy tablicę F o n wierszach i E + 1 kolumnach
# F[i][b] mówi nam jaki jest optymalny koszt znalezienia się na planecie i mając b ton paliwa w baku
# Najpierw sprawdzamy czy opłaca się tankować kolejne litry paliwa do baku, następnie czy opłaca się
# teleportować, a na końcu czy opłaca się dolecieć na planety w aktualnym zasięgu. Złożoność czasową
# algorytmu szacuję na O(n^2 * E), a pamięciową na O(nE)


def planets( D, C, T, E ):
    n = len(D)
    F = [[float('inf') for _ in range(E + 1)] for _ in range(n)] # F[i][b] najmniejszy koszt znalezienia się na planecie i mając b w baku

    F[0][0] = 0 # planeta A, 0 litrów paliwa

    for i in range(n):
        for b in range(1, E + 1): # sprawdzamy czy opłaca się tankować 1, 2, ..., E ton paliwa
            F[i][b] = min(F[i][b], F[i][b - 1] + C[i])

        if i < T[i][0]: # jeśli opłaca się teleportować
            F[T[i][0]][0] = min(F[T[i][0]][0], F[i][0] + T[i][1])

        for j in range(i + 1, n): # rozważamy przelot z i na i + 1, i + 2, ..., n - 1 planetę
            distance = D[j] - D[i]
            for k in range(distance, E + 1):
                F[j][k - distance] = min(F[j][k - distance], F[i][k])

    return min(F[n - 1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
