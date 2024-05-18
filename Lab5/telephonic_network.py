from queue import Queue
# Operotor sieci komórkowej, której maszty tworzą graf spójny chce ją wyłączyć
# wyłączając po kolei każdy maszt tak aby graf pozostał spójny. Napisz program
# wypisujący maszty w kolejności ich wyłączania.
def turn_off_net_dfs(G): # O(V + E)
    def DFSVisit(G, u, visited):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v, visited)
                print(v, end=' ')
    n = len(G)
    visited = [False for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u, visited)
            print(u, end=' ')
    print()
def sort(T):
    def quick_sort(T, left, right):
        if left > right: return
        pivot = (left + right) // 2
        pivot = partition(T, left, right, pivot)
        quick_sort(T, left, pivot - 1)
        quick_sort(T, pivot + 1, right)
    def partition(T, left, right, p_index):
        pivot = right
        T[p_index], T[right] = T[right], T[p_index]
        ind = left - 1
        for i in range(left, right):
            if T[i][0] < T[pivot][0] or (T[i][0] == T[pivot][0] and T[i][1] < T[pivot][1]):
                ind += 1
                T[i], T[ind] = T[ind], T[i]
        ind += 1
        T[ind], T[pivot] = T[pivot], T[ind]
        return ind
    return quick_sort(T, 0, len(T) - 1)
def turn_off_net_bfs(G):
    n = len(G)
    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)]
    visited[0] = True
    Q = Queue()
    Q.put(0)
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                d[v] = d[u] + 1
                visited[v] = True
                Q.put(v)
    result = [(d[i], i) for i in range(n)]
    sort(result)
    array = [result[i][1] for i in range(n - 1, -1, -1)]
    print(array)

G = [
    [2, 3],
    [2, 6],
    [0, 1],
    [0, 4, 5, 6],
    [1, 3, 5, 8],
    [3, 4],
    [1, 3],
    [8],
    [4, 7]
]
turn_off_net_bfs(G)