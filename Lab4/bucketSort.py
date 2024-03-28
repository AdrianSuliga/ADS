# sort numbers from interval 0 to 1 in linear time
# numbers are distributed equally across given interval.
from random import randrange
def bucket_sort(T):
    n = len(T)
    buckets = [[] for _ in range(n)]

    for i in range(n):
        buckets[int(n*T[i])].append(T[i])
    
    for i in range(n):
        insertion_sort(buckets[i])
    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            T[k] = buckets[i][j]
            k += 1

def insertion_sort(T):
    n = len(T)
    for i in range(1, n):
        j = i - 1
        to_insert = T[i]
        while j > -1 and to_insert < T[j]:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = to_insert 

def gen_array(n):
    T = [randrange(1, 100) for _ in range(n)]
    for i in range(n): T[i] /= 100
    return T

n = int(input("n="))
T = gen_array(n)
print(T)
bucket_sort(T)
print(T)