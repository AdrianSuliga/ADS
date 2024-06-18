from zad10ktesty import runtests
from math import inf

# Adrian Suliga
# f(i) - najmniejsza liczba dywanów potrzebnych do pokrycia i powierzchni
# f(i) = min { f(i - j*j) | 1 <= j <= sqrt(i) } + 1

def dywany(N):
    F = [inf for _ in range(N + 1)]
    F[1] = 1

    F[N] = f(N, F)
    
    print(F)

    return []

def f(i, F): # O(n * sqrt(n))
    if F[i] != inf: return F[i]
    if i == 1 or i == 0: return i

    result = inf
    for j in range(1, int(i**(0.5)) + 1):
        if i - j**2 < 0: break
        result = min(result, f(i - j**2, F) + 1)

    F[i] = result
    return result

# Podejście rekurencyjne ze słownikiem
"""def dywany ( N ):
    print(N)
    res = f(N, {})
    return res

def f(target, memo):
    m = int(target**(0.5))
    if target in memo: return memo[target]
    if target == 0: return []

    best_len, result = inf, []

    for i in range(m, 0, -1):
        if target < i**2: continue
        reminder = f(target - i**2, memo)
        reminder.append(i)
        if best_len > len(reminder):
            best_len = len(reminder)
            result = list(reminder)
        reminder = []
    
    memo[target] = result
    return result"""

#runtests( dywany )
print(dywany(6))