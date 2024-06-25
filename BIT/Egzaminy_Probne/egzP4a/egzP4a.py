from egzP4atesty import runtests 

# Adrian Suliga
# Algorytm sortuje połączenia po pierwszej liczbie w krotce, następnie szuka
# najdłuższego rosnącego podciągu wśród drugich liczb w krotkach w czasie O(n logn)
# Szacuję złożoność czasową algorytmu na O(nlogn), a pamięciową na O(n)

def mosty( T:list ) -> int:
    n = len(T)
    T.sort(key = lambda x : x[0])
    A = [T[i][1] for i in range(n)]
    return LIS(A)

def LIS(A):
    n = len(A)
    R, cnt = [A[0]], 1

    for i in range(1, n):
        if A[i] > R[cnt - 1]: 
            R.append(A[i])
            cnt += 1
        else: 
            R[bin_search(R, A[i], 0, len(R) - 1)] = A[i]
    
    return len(R)        

def bin_search(R, val, left, right):
    if left > right: return left
    pivot = (left + right) // 2

    if R[pivot] < val:
        return bin_search(R, val, pivot + 1, right)
    else:
        return bin_search(R, val, left, pivot - 1)

# Adrian Suliga, podejście klasyczne, n^2
# Algorytm sortuje tablicę po pierwszej liczbie każdej z krotek, następnie na tak posortowanej
# tablicy wykonujemy algorytm szukania najdłuższego rosnącego podciągu wśród drugich liczb każdej
# z krotek. Szacuję złożoność czasową algorytmu na O(n^2) a pamięciową na O(n).

# f(i) - długość najdłuższego rosnącego podciągu kończącego się na T[i]
# f(i) = max { f(j) + 1 | j < i i T[j] < T[i] }

"""def mosty ( T:list ):
    T.sort(key = lambda x : x[0])
    n = len(T)
    F = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if T[j][1] <= T[i][1]:
                F[i] = max(F[i], F[j] + 1)

    return max(F)"""

runtests ( mosty, all_tests=True )
