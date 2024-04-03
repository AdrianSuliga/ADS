from zad2testy import runtests
# Adrian Suliga
# Gdyby tablica S była posortowana malejąco, to maksymalna ilość śniegu jaki możemy uzyskać to suma od 0. do (n-1). elementu
# przy czym wartość i. elemntu pomniejszamy o i czyli ilość dni, jakie upłynęły.

def build_heap(S):
    n = len(S)
    for i in range(parent(n - 1), -1, -1):
        heapify(S, n, i)
def heapify(S, n, i):
    l, r = left(i), right(i)
    mi = i
    if l < n and S[l] > S[mi]: mi = l
    if r < n and S[r] > S[mi]: mi = r
    if mi != i:
        S[mi], S[i] = S[i], S[mi]
        heapify(S, n, mi)

def parent(i): return (i - 1) // 2
def left(i): return 2 * i + 1
def right(i): return 2 * i + 2

def snow( S ):
    n = len(S)
    result, days = 0, 0
    build_heap(S)
    for i in range(n - 1, 0, -1):
        if S[0] - days > 0: result += S[0] - days
        else: break # jesli cały śniego się stopił to nie ma co szukać dalej
        S[0], S[i] = S[i], S[0]
        days += 1
        heapify(S, i, 0)
    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
