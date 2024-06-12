from zad1ktesty import runtests

# Adrian Suliga
# Algorytm oblicz wartości dla poniżej zdefiniowanej funkcji:
# f(i, j) = różnica ilości zer i jedynek dla S[i : j + 1]
# f(i, j) = f(i, j - 1) +- 1 zależnie czy S[j] == 0 czy S[j] == 1
# f(i, i) = 1 dla S[i] == 0
# f(i, i) = -1 dla S[i] == 1
# f(i, j) = -1 gdy i > j
# Złożoność czasową i pamięciową algorytmu szacuję na O(n^2) z powodu zagnieżdżonych
# w sobie pęli .

def roznica( S ):
    n, result = len(S), -1
    F = [[-1 for _ in range(n)] for _ in range(n)] # Tablica na wartości funkcji f(i, j)

    for i in range(n): # warunki początkowe dla każdego wiersza
        if S[i] == '0': F[i][i] = 1
        else: F[i][i] = -1

    for i in range(n):
        for j in range(i + 1, n):
            F[i][j] = F[i][j - 1]
            if S[j] == '0': F[i][j] += 1
            else: F[i][j] -= 1
            result = max(result, F[i][j])

    return result
 
runtests ( roznica )