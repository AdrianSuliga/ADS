from random import randint
def radix_sort(T):
    n = len(T)
    B = [0 for _ in range(n)]
    C = [0 for _ in range(n)]

    for i in range(n): C[T[i] % n] += 1

    for i in range(1, n): C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[T[i] % n] - 1] = T[i]
        C[T[i] % n] -= 1

    for i in range(n): C[i] = 0

    for i in range(n): C[T[i] // n] += 1

    for i in range(1, n): C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[T[i] // n] -= 1
        B[C[T[i] // n]] = T[i]
    
    for i in range(n): T[i] = B[i]


n = int(input("n="))
T = [randint(1, n*n-1) for _ in range(n)]
print(T)
radix_sort(T)
print(T)

