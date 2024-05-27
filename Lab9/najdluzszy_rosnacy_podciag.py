# funkcja f(k) określa długość najdłuższego rosnącego podciągu kończącego się na A[k]

# f(k) = max { f(t) + 1; t < k i A[t] < A[k] }
# max bo interesuje nas najdłuższy podciąg, dodajemy 1 do f(t) dla t < k i A[t] < A[k] bo rozważamy sytuację gdy do
# już rosnącego podciągu liczb z przedziału [0, ..., t] dodajemy k

def LIS(A:list) -> tuple:
    n = len(A)
    F = [1 for _ in range(n)]
    P = [None for _ in range(n)]

    for k in range(1, n):
        for t in range(k):
            if A[t] < A[k] and F[k] < F[t] + 1:
                F[k] = F[t] + 1
                P[k] = t
    return F, P

def print_solution(F:list, P:list, k:int) -> None:
    if P[k] != None: print_solution(F, P, P[k])
    print(F[k])

A = [2, 1, 4, 3, 4, 8, 5, 7, 1]

F, P = LIS(A)
print_solution(A, P, 7)