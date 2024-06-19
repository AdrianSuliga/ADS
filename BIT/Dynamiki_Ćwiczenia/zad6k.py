from zad6ktesty import runtests 

# Adrian Suliga
# f(i) - maksymalna ilość zakodowań dla S[:i + 1]
# Wzór rekurencyjny na f(i) jest trudny do zapisania ze względu na skomplikowane warunki
# zamiast tego opiszmy to w ten sposób:
# f(i) := 0
# jeśli S[i] != '0': f(i) += f(i - 1)
# jeśl dwa ostatnie znaki w S[i] to liczby z przedziału [10; 26]: f(i) += f(i - 2)
# Szacuję złożoność czasową i pamięciową algorytmu na O(n)

def haslo ( S ):
    n = len(S)
    F = [0 for _ in range(n)]
    
    F[0] = 1
    if int(S[:2]) < 27:
        F[1] = 2
    else: F[1] = 1

    for i in range(2, n):
        if S[i] != '0':
            F[i] += F[i - 1]
        if 10 <= int(S[i - 1 : i + 1]) < 27:
            F[i] += F[i - 2]
    
    return F[n - 1]

runtests ( haslo )