from kol1testy import runtests

def maxrank(T): # nlogn z błędem przy edge casie, w którym wiele razy powtarza się jednak liczba
    n = len(T)
    G = [(T[i], i) for i in range(n)]
    pulled_numbers_cnt = 0
    max_rank = -1
    heap_size = n
    prev_ind = -1
    
    build_heap(G)

    while heap_size > 0:
        element = pop_front(G)
        if element[1] > prev_ind:
            max_rank = max(max_rank, element[1] - pulled_numbers_cnt)
            prev_ind = element[1]
        
        pulled_numbers_cnt += 1
        heap_size -= 1
        
    return max_rank
    
def pop_front(G):
    G[0], G[-1] = G[-1], G[0]
    element = G.pop()
    heapify(G, len(G), 0)
    return element
def build_heap(T:list) -> None:
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)
        
def heapify(T, n, i):
    l, r, mi = left(i), right(i), i
    if l < n and T[l][0] > T[mi][0]: mi = l
    if r < n and T[r][0] > T[mi][0]: mi = r
    if mi != i:
        T[mi], T[i] = T[i], T[mi]
        heapify(T, n, mi)
        
def left(i): return 2 * i + 1
def right(i): return 2 * i + 2
def parent(i): return (i - 1) // 2

"""def maxrank(T): # Optimized n^2 solution
    n = len(T)

    is_outranked = [False for _ in range(n)]

    max_rank = -1
    for i in range(n - 1, -1, -1):
        if is_outranked[i]: continue
        rank = 0
        for j in range(i):
            if T[j] < T[i]: 
                is_outranked[j] = True
                rank += 1
        max_rank = max(max_rank, rank)
        if max_rank > i: break
    return max_rank"""
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
