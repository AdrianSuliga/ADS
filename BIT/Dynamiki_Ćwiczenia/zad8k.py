from zad8ktesty import runtests 

# Adrian Suliga
# Algorytm oblicza wartości następującej funkcji:
# f(i, j) - funkcja określająca ilość kroków wymaganych do przekształcenia
# napisu s[:i + 1] na napis t[:j + 1]
# f(i, j) = f(i - 1, j - 1) gdy s[i] == s[j]
# f(i, j) = min { f(i - 1, j), f(i - 1, j - 1), f(i, j - 1) } + 1
# f(0, j) = j
# f(i, 0) = i  

def napraw(s, t):
    n, m = len(s), len(t)
    return f(m, n, t, s, {})

def f(i, j, stri, strj, memo):
    if (i, j) in memo: return memo[(i, j)]
    if i == 0: return j
    if j == 0: return i

    if stri[i - 1] == strj[j - 1]:
        result = f(i - 1, j - 1, stri, strj, memo)
    else:
        result = min(f(i - 1, j, stri, strj, memo), f(i - 1, j - 1, stri, strj, memo), f(i, j - 1, stri, strj, memo)) + 1

    memo[(i, j)] = result
    return result

"""def napraw ( s, t ):
    n, m = len(s), len(t)
    F = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for j in range(1, n + 1):
        F[0][j] = j
    for i in range(1, m + 1):
        F[i][0] = i

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if s[j - 1] == t[i - 1]:
                F[i][j] = F[i - 1][j - 1]
            else:
                F[i][j] = min(F[i - 1][j], F[i - 1][j - 1], F[i][j - 1]) + 1

    return F[m][n]"""

runtests ( napraw )