from random import randint
def quick_select(T, left, right, k):
    if left >= right:
        return T[left]
    pInd = randint(left, right)
    pInd = partition(T, left, right, pInd)

    if k == pInd:
        return T[k]
    elif k < pInd:
        return quick_select(T, left, pInd - 1, k)
    else:
        return quick_select(T, pInd + 1, right, k)

def partition(T, left, right, pInd):
    pivot = right
    T[pInd], T[right] = T[right], T[pInd]
    index = left - 1
    for i in range(left, right):
        if T[i] <= T[pivot]:
            index += 1
            T[i], T[index] = T[index], T[i]
    index += 1
    T[pivot], T[index] = T[index], T[pivot]
    return index

T = [randint(1, 100) for _ in range(10)]
print(T)
print(quick_select(T, 0, len(T) - 1, 1))