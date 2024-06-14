from zad5ktesty import runtests

# f(i, j) = (maksymalna suma obecnego gracza, maksymalna suma następnego gracza)
# f(i, i) = (T[i], 0)
# f(i - 1, i) = (max(T[i - 1], T[i]), min(T[i - 1], T[i]))
# f(i, j) = max { T[i] + f(i + 1, j)[1], T[j] + f(i, j - 1)[1] }

def garek ( A ):
    n = len(A)
    memo = {}

    return f(A, 0, n - 1, memo)[0]

def f(A:list, i:int, j:int, memo:dict) -> tuple:
    if (i, j) in memo: return memo[(i, j)]
    if i == j: return (A[i], 0)
    if i + 1 == j: return (max(A[i], A[j]), min(A[i], A[j]))

    tup1 = f(A, i + 1, j, memo)
    tup2 = f(A, i, j - 1, memo)

    if A[i] + tup1[1] > A[j] + tup2[1]:
        res = A[i] + tup1[1], tup1[0]
    else:
        res = A[j] + tup2[1], tup2[0]

    memo[(i, j)] = res
    return res

runtests ( garek )
# 8 15 3 7