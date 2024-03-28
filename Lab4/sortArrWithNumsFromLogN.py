# Liczby są ze zbioru B; |B| = log(n), posortować możliwie jak najszybciej
# uzyskana złożoność: O(n log(log(n)))
from math import log10
from random import randrange
def sort(T):
    n = len(T)
    result = []
    for i in range(n):
        extracted = binary_search(result, T[i], 0, len(result) - 1)
        if extracted[0]: result[extracted[1]] = (result[extracted[1]][0], result[extracted[1]][1] + 1)
        else: result = result[:extracted[1]] + [(T[i], 1)] + result[extracted[1]:]
    k = 0
    for i in range(len(result)):
        for j in range(result[i][1]):
            T[k] = result[i][0]
            k += 1

def binary_search(T, val, left, right):
    n = len(T)
    while True:
        pivot = (left + right) // 2
        if left > right: return (False, pivot + 1)
        if T[pivot][0] == val: return (True, pivot)
        elif T[pivot][0] < val: left = pivot + 1
        else: right = pivot - 1

def gen_array(n):
    T = [0 for _ in range(n)]
    num = randrange(100)
    for i in range(n):
        T[i] = randrange(num, int(num + log10(n)) + 1)
    return T

n = int(input("n="))
T = gen_array(n)
print(T)
sort(T)
print(T)