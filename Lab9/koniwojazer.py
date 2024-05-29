# traveling salesperson
# C - zbiór miast
# d: CxC -> R_+  - odległości między miastami
# znaleźć trasę tak aby wrócić do punktu startowego,
# odwiedzić wszystkie miasta i pokonać możliwie jak najkrótszą trasę

# problem jest NP zupełny
# brute force to O(n!)

# można go zoptymalizować programowaniem dynamicznym:
# S zawarte w C i s i t należą do S
# f(S, t) - najkrótsza trasa od startu do t przechodząca przez wszystkie
# miasta w S
# rozwiązaniem jest wówczas min { f(C, t) + d(t, 0) | t należy do C \ {0} }
# f(S, t) = min { f(S \ {t}, r) + d(r, t) | r należy do S \ {t} }
# złożoność takiego rozwiązania to O(2^n * n^2)

# wersja bitoniczna problemu:
# miasta są w R^2, najpierw wędrujemy tylko w prawo,
# potem tylko w lewo
# f(i, j) - koszt ścieżek z x_0 do x_i oraz z x_0 do x_j które wykorzystują
# wszystkie ściezki z x_0 ... x_i i x_0 ... x_j nie powtarzając żadnej
# rozwiązaniem jest min { f(i, n - 1) + d(i, n - 1) | i należy do C \ {0} }

# Gdy i < j - 1:
# f(i, j) = f(i, j - 1) + d(x_(j-1), x_j)

# Gdy i = j - 1:
# f(j - 1, j) = min { f(i, j - 1) + d(x_i, x_j) | gdzie i < j - 1 } 

def salesperson(d:list, s:int, n:int):
    F = [[float('inf') for _ in range(n)] for _ in range(n)]


def tspf(i:int, j:int, F:list, D:list):
    if F[i][j] != float('inf'): return F[i][j]
    if i == j - 1:
        minimum = float('inf')
        for k in range(j - 1):
            minimum = min(minimum, tspf(k, j - 1, F, D) + D[k][j])
        F[i][j] = minimum
    elif i < j - 1:
        F[i][j] = tspf(i, j - 1, F, D) + D[j - 1][j]

    return F[i][j] 
