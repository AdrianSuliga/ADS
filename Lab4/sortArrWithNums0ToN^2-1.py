# given array of n integers from range 0 ... n^2 - 1 sort them in linear time
# solution: sort by T[i] % n, than sort by T[i] // n
from random import randint
from time import time
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

    for i in range(n): C[B[i] // n] += 1
    for i in range(1, n): C[i] += C[i - 1]

    for i in range(n - 1, -1, -1): 
        T[C[B[i] // n] - 1] = B[i]
        C[B[i] // n] -= 1

n = int(input("n="))
T = [randint(1, n*n-1) for _ in range(n)]
start = time()
radix_sort(T)
end = time()
print(end - start)