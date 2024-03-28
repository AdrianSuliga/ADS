from random import randrange
def radix_sort(T):
    n = len(T)

    max_size = 0
    for i in range(n): max_size = max(max_size, len(T[i])) # O(n) to find index to start sorting from

    for i in range(max_size - 1, -1, -1): # O(k * O(n)) = O(nk) to sort items
        sort(T, i)

def sort(T, ind): # O(n) in total
    n = len(T)
    B = [None for _ in range(n)]
    C = [0 for _ in range(27)]

    for i in range(n):
        if len(T[i]) - 1 < ind:
            C[26] += 1
        else:
            C[ord(T[i][ind]) - ord('a')] += 1
    for i in range(1, 27): C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        if len(T[i]) - 1 < ind:
            B[C[26] - 1] = T[i]
            C[26] -= 1
        else:
            B[C[ord(T[i][ind]) - ord('a')] - 1] = T[i]
            C[ord(T[i][ind]) - ord('a')] -= 1

    for i in range(n): T[i] = B[i]

def gen_string(length):
    result = ""
    for _ in range(length):
        result += str(chr(randrange(ord('a'), ord('z') + 1)))
    return result
def gen_array(n):
    result = []
    for _ in range(n):
        result.append(gen_string(randrange(3, 15)))
    return result

n = int(input("n="))
T = gen_array(n)
print(T)
radix_sort(T)
print(T)