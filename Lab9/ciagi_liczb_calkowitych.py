# A - ciąg liczb naturalnych
# T - liczba naturalna
# czy istnieje podciąg A, taki że jego suma równa się T

# f(x, k) - czy istnieje podciąg A kończący się na max. k, który sumuje się do x
# f(x, k) = f(x - A[k - 1], k - 1) or f(x, k - 1)
# f(0, k) = True
# f(x, 0) = False

def dyn_sum(A:list, Target:int, CurrentIndex:int, Memo:dict) -> bool:
    if (Target, CurrentIndex) in Memo: return Memo[(Target, CurrentIndex)]
    if Target == 0: return True
    if CurrentIndex == 0: return False

    Memo[(Target, CurrentIndex)] = dyn_sum(A, Target, CurrentIndex - 1, Memo) or dyn_sum(A, Target - A[CurrentIndex - 1], CurrentIndex - 1, Memo)
    return Memo[(Target, CurrentIndex)]

def tab_sum(A:list, T:int, k:int) -> bool:
    F = [[None for _ in range(k + 1)] for _ in range(T + 1)]

    for i in range(k + 1):
        F[0][i] = True
    for i in range(1, T + 1):
        F[i][0] = False

    for t in range(1, T + 1):
        for x in range(1, k + 1):
            F1, F2 = False, False
            if t - A[x - 1] >= 0:
                F1 = F[t - A[x - 1]][x - 1]
            F2 = F[t][x - 1]
            F[t][x] = F1 or F2

    return F[T][k]

A = [7, 2, 9, 13, 4, 22, 6]
T = 30
print(tab_sum(A, T, len(A)))