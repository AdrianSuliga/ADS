from time import time
def fib_brute(n:int) -> int: # O(2^n) czasowo, O(2^n) pamięciowo
    if n <= 1: return 1
    return fib_brute(n - 1) + fib_brute(n - 2)

def fib_dyn(n:int) -> int: # O(n) czasowo, O(n) pamięciowo
    A = [0 for _ in range(n + 1)]
    A[0], A[1] = 1, 1

    for i in range(2, n + 1):
        A[i] = A[i - 1] + A[i - 2]
    
    return A[n]

def fib_best(n:int) -> int: # O(n) czasowo, O(1) pamięciowo
    fibL, fibM, fibR = 0, 1, 1

    for _ in range(n - 1):
        fibL = fibM
        fibM = fibR
        fibR = fibM + fibL
    
    return fibR

start = time()
print(fib_best(20000))
end = time()

print("\nBEST: ", end - start, '\n')

start = time()
print(fib_dyn(20000))
end = time()

print("\nDYNAMIC: ", end - start, '\n')