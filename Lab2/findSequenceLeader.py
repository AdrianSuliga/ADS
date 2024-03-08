"""
lider - liczba występująca na więcej niż połowie pozycji
dana jest nieposortowana tablica, znajdź lidera (jeśli istnieje)
"""
def findLeader(T): # O(2*n) - dwa przejścia przez tablicę
    n = len(T)
    leader, cnt = T[0], 1
    for i in range(n):
        if T[i] != leader:
            cnt -= 1
        else:
            cnt += 1
        if cnt < 0:
            leader = T[i]
    cnt = 0
    for i in range(n):
        if T[i] == leader:
            cnt += 1
    return cnt > n // 2

T = [2, 3, 2, 2, 2, 4, 2, 3, 2, 8, 9, 2]
print(findLeader(T))