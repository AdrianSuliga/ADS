"""
policz ilość inwersji w tablicy
"""
def merge_arrays(T1:list, T2:list, T:list):
    n = len(T1)
    i, j = 0, 0
    cnt = 0
    T1.append(float('inf'))
    T2.append(float('inf'))
    for k in range(2*n):
        if T1[i] < T2[j]:
            T[k] = T1[i]
            i += 1
        else:
            T[k] = T2[j]
            j += 1
            cnt += n - i
    return cnt