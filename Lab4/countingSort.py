# Array T of size n has values in range 0 ... 2n. Sort it in linear time
from random import randrange
def counting_sort(T):
    n = len(T)

    C = [0 for _ in range(2*n)]
    B = [None for _ in range(n)]

    for i in range(n): C[T[i]] += 1
    for i in range(1, 2*n): C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[T[i]] - 1] = T[i]
        C[T[i]] -= 1

    for i in range(n): T[i] = B[i]


n = int(input("n="))
T = [randrange(0, 2*n) for _ in range(n)]
print(T)
counting_sort(T)
print(T)