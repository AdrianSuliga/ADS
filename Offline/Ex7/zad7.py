from zad7testy import runtests
from math import inf

# Adrian Suliga
# Algorytm oblicz funkcją f(i, j, m) gdzie i, j oznacza komnatę w jakiej się znajdujemy a m czy weszliśmy do tej
# komnaty od góry (0) czy od dołu (1). wartościami funkcji jest maksymalna liczba komnat jaką można odwiedzić przed
# dotarciem do (i, j). Najpierw staramy się dojść jak najdalej w dół w kolumnie 0. Następnie dla każdej następnej kolumny
# j + 1 przepisujemy max { f(i, j, 0), f(i, j, 1) }. Po przepisaniu musimy spróbować w optymalny sposób przemierzyć labirynt
# w nowej kolumnie. Najpierw idziemy od góry szukając maksymalnej liczby komnat, następnie od dołu. Szacuję złożoność czasową
# algorytmu na O(n^2), a pamięciową też na O(n^2).

def maze( L ):
    n = len(L) # F[i][j][0] - max. liczba komnat jakie można odwiedzić po drodze do (i, j)
    F = [[(-inf, -inf) for _ in range(n)] for _ in range(n)] # jeśli ostatecznie wejdziemy do (i, j) od góry 
    
    F[0][0] = (1, 1)
    
    for i in range(1, n):
        if L[i][0] == '#': break
        F[i][0] = (F[i - 1][0][0] + 1, F[i][0][1])

    for j in range(1, n):
        for i in range(n):
            if L[i][j] != '#':
                num = max(F[i][j - 1][0] + 1, F[i][j - 1][1] + 1)
                F[i][j] = (num, num)
        
        for i in range(1, n):
            if L[i][j] != '#' and F[i - 1][j][0] != -inf:
                F[i][j] = (max(F[i][j][0], F[i - 1][j][0] + 1), F[i][j][1])

        for i in range(n - 2, -1, -1):
            if L[i][j] != '#' and F[i + 1][j][1] != -inf:
                F[i][j] = (F[i][j][0], max(F[i][j][1], F[i + 1][j][1] + 1))
        
    num = max(F[n - 1][n - 1]) - 1
    if num == -inf: return -1
    return num

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )