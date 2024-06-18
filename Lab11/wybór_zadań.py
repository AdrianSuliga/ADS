from random import randint
# Dana jest lista krotek reprezentujących przedziały
# wybrać jak najwięcej przedziałów tak aby się nie pokrywały

# Problem można rozwiązać następującym algorytmem zachłannym
# 1. sortujemy przedziały po drugim końcu przedziału
# 2. wybieramy najwcześniejszy przedział
# 3. ignorujemy wszystie nachodzące na niego, szukamy następnego
# najwcześniej się kończącego

# Czemu możemy wybrać najwcześniejszy przedział?
# Gdy rozwiązanie optymalne zawiera ten przedział to nic to zmienia
# Gdy rozwiązanie optymalne nie zawiera najwcześniejszego przedziału
# to bierzemy najwcześniejszy przedział z rozwiązania optymalnego i zamieniamy
# z najwcześniejszym w całej tablicy. Przedział najwcześniejszy przecina się 
# dokładnie z jednym z rozwiązania optymalnego więc nie psuje nam to rozwiązania

def greedy_task(P):
    n = len(P)
    special_sort(P)
    print(P)

    current = P[0]
    result = [current]

    for i in range(1, n):
        if P[i][0] <= current[1]: continue
        result.append(P[i])
        current = P[i]

    return result

def special_sort(P):
    n = len(P)
    build_heap(P)
    for i in range(n - 1, 0, -1):
        P[0], P[i] = P[i], P[0]
        heapify(P, i, 0)

def build_heap(P):
    n = len(P)
    for i in range((n - 2) // 2, -1, -1):
        heapify(P, n, i)

def heapify(T, n, i):
    l, r, mi = 2 * i + 1, 2 * i + 2, i

    if l < n and T[l][1] > T[mi][1]: mi = l
    if r < n and T[r][1] > T[mi][1]: mi = r

    if mi != i:
        T[mi], T[i] = T[i], T[mi]
        heapify(T, n, mi)

def validate(P):
    Res = []
    for a, b in P:
        if a >= b: continue
        Res.append((a, b))
    return Res

n = 30
P = [(randint(1, 100), randint(1, 100)) for _ in range(n)]
P = validate(P)
print(greedy_task(P))