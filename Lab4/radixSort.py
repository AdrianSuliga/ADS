# Given array of strings, sort them in alphabetical order. Every string has the same length
from random import randrange

def counting_sort(T, ind):
    n = len(T)
    B = [None for _ in range(n)]
    C = [0 for _ in range(26)]
    for i in range(n):
        C[ord(T[i][ind]) - ord('a')] += 1
    for i in range(1, 26):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        B[C[ord(T[i][ind]) - ord('a')] - 1] = T[i]
        C[ord(T[i][ind]) - ord('a')] -= 1
    for i in range(n): T[i] = B[i]
    
def radix_sort(T):
    n = len(T)
    
    for i in range(len(T[0]) - 1, -1, -1):
        counting_sort(T, i)

def gen_string(dl):
    result = ""
    for i in range(dl):
        rand_char = str(chr(randrange(ord('a'), ord('z'))))
        result += rand_char
    return result

def gen_array(n, l):
    result = []
    for i in range(n):
        result.append(gen_string(l))
    return result

n = int(input("n="))
l = int(input("char length="))
T = gen_array(n, l)
print(T)
radix_sort(T)
print(T)