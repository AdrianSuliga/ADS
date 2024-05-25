def LIS(A:list) -> tuple:
    n = len(A)
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]

    for k in range(1, n):
        for t in range(k):
            if A[t] < A[k] and F[k] < F[t] + 1:
                F[k] = F[t] + 1
                P[k] = t
    return F, P

def print_solution(F:list, P:list, k:int) -> None:
    if P[k] != -1:
        print(F, P, P[k])
    print(F[k])

A = [2, 1, 4, 3, 4, 8, 5, 7]

F, P = LIS(A)
print_solution(F, P, 7)