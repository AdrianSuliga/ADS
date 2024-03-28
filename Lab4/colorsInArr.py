from random import randrange
def find_colors(T, k):
    n = len(T)
    found_colors = []
    min_dist = float('inf')
    res = 0, 0
    i, j = 0, 0
    while j < n:
        while len(found_colors) < k and j < n:
            extract = binary_search(found_colors, T[j], 0, len(found_colors) - 1)
            if extract[0]: found_colors[extract[1]] = (found_colors[extract[1]][0], found_colors[extract[1]][1] + 1)
            else: found_colors = found_colors[:extract[1]] + [(T[j], 1)] + found_colors[extract[1]:]
            j += 1
        while len(found_colors) == k:
            extract = binary_search(found_colors, T[i], 0, k - 1)
            found_colors[extract[1]] = (found_colors[extract[1]][0], found_colors[extract[1]][1] - 1)
            if found_colors[extract[1]][1] == 0:
                found_colors.pop(extract[1])
                break
            i += 1
        if j - i < min_dist:
            min_dist = j - i
            res = i, j - 1
        i += 1
    return res

def binary_search(T, val, left, right):
    while True:
        pivot = (left + right) // 2
        if left > right: return (False, pivot + 1)
        if T[pivot][0] == val: return (True, pivot)
        elif T[pivot][0] < val: left = pivot + 1
        else: right = pivot - 1

def gen_array(n, k):
    return [randrange(k) for _ in range(n)]


n = int(input("n="))
k = int(input("k="))
T = gen_array(n, k)
print(T)
print(find_colors(T, k))