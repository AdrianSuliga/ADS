# znajduje najkrótsze ścieżki, jeśli w grafie
# występuje cykl ujemny to zwraca pustą listę
def shortest_path(G:list, s:int, e:int) -> list:
    n = len(G)
    d = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    d[s] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, cost in G[u]:
                if d[u] + cost < d[v]:
                    d[v] = d[u] + cost
                    parent[v] = u
    
    for u in range(n):
        for v, cost in G[u]:
            if d[v] > d[u] + cost:
                return []

    result = []
    result.append(e)
    buffor = parent[e]
    while buffor != None and buffor != s:
        result.append(buffor)
        buffor = parent[buffor]
    result.append(s)
    reverse(result)
    return result

def reverse(T:list) -> None:
    i, j = 0, len(T) - 1
    while i < j:
        T[i], T[j] = T[j], T[i]
        i += 1
        j -= 1

G = [
    [(1, 1)],
    [(0, 1), (2, -2), (5, -3), (6, 5)],
    [(3, 7), (4, 1)],
    [(2, 7), (4, 9)],
    [(2, 1), (3, 9)],
    [(6, 1), (9, 10)],
    [(5, 1), (7, 2), (8, 5), (1, 5)],
    [(6, 2), (8, 4)],
    [(6, 5), (7, 4), (9, -8)],
    [(5, 10)]
]
print(shortest_path(G, 0, 9))