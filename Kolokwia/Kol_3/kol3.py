from kol3testy import runtests
from math import inf

# Adrian Suliga
# Algorytm oblicza wartości następującej funkcji:
# f(i, sum) - minimalna liczba drzew jakie należy wyciąć aby uzyskać sumę podzielną przez m gdy rozważamy drzewa do i.
# Drzewo i. mogę wyciąć lub nie
# f(i, sum) = min { f(i - 1, sum), f(i - 1, sum - T[i]) + 1}
# f(i, sum) = 0 gdy sum % m == 0
# f(i, sum) = inf gdy i < 0
# Przy takiej deklaracji odpowiedzią do zadania jest f(n - 1, sum)
# Kluczowe do efektywnego obliczenia wartości f jest skorzystanie z praw arytmetyki modulo,
# pewna suma liczb a1 + a2 + ... an jest podzielna przez m wtedy i tylko wtedy gdy
# (a1 % m) + (a2 % m) + ... + (an % m) jest podzielna przez m, co w naszym algorytmie oznacza
# że nie musimy prowadzić obliczeń na wartościach z tablicy T, a wystarczy nam dla każdego
# i rozważyć T[i] % m. Dodatkowo w celu efektywnego obliczania wartości funkcji f algorytm
# spamiętuje widziane już wartości w tablicy sum x n.
# Szacuję złożoność czasową i pamięciową algorytmu na O(n^3)

def orchard(T, m):
    n = len(T)
    sum = 0
    for i in range(n):
        T[i] %= m
    for t in T: sum += t # suma będzie maksymalnie wynosić mn, czyli będzie co do stałej równa n^2

    F = [[-1 for _ in range(sum + 1)] for _ in range(n)] # mamy n^2 * n możliwych wartości funkcji f

    return f(n - 1, sum, m, T, F)

def f(i, target, m, T, F):
    if F[i][target] != -1: return F[i][target]
    if target % m == 0: return 0
    if i < 0: return inf

    result = min(f(i - 1, target, m, T, F), f(i - 1, target - T[i], m, T, F) + 1)
    F[i][target] = result
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)