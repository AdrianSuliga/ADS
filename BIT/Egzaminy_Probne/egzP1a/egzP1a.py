from egzP1atesty import runtests 
from math import inf

# Adrian Suliga
# Algorytm oblicza wartości następującej funkcji
# f(i) - minimalna ilość liter potrzebnych do zakodowania wiadomości jeśli rozważamy tylko 
# litery od 0. do i.
# f(i) = min { f(i - len(L[j])) + 1 | L[j] to kolejne rozpoznawane przez telegraf znaki } gdzie i - len(L[i]) >= 0
# f(i) = inf gdy i < 0
# Rozwiązaniem zadania jest wówczas f(n - 1)
# W celu przyspieszenia obliczeń algorytm spamiętuje wartości f() podczas zejść rekurencyjnch
# Szacuję złożoność czasową algorytmu na O(mn), a pamięciową na O(m + n)

def titanic(W, M, D): # podejście iteracyjne
    message = morse_form(W, M)
    D = [(M[d][1], len(M[d][1])) for d in D]
    n, m = len(message), len(D)
    F = [inf for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if message[: i + 1] == D[j][0]:
                F[i] = 1
            if message[i - D[j][1] + 1 : i + 1] == D[j][0]:
                F[i] = min(F[i], F[i - D[j][1]] + 1)         

    return F[n - 1]

# Podejście rekurencyjne ze spamiętywaniem
"""def titanic( W, M, D ):
    message = morse_form(W, M)
    D = [M[d][1] for d in D]
    n = len(message)
    F = [-1 for _ in range(n)]

    return f(n - 1, message, D, F)

def f(i, message, D, F):
    if F[i] != -1: return F[i]
    for sign in D:
        if message[:i + 1] == sign: return 1

    result = inf
    for sign in D:
        strlen = len(sign)
        if message[i - strlen + 1 : i + 1] == sign:
            result = min(result, f(i - strlen, message, D, F) + 1)

    F[i] = result
    return result"""

def morse_form(W, M):
    result = ""
    for letter in W:
        result += M[ord(letter) - ord('A')][1]
    return result

runtests ( titanic, recursion=True )
"""W = "SOS"
D = [0, 4, 13, 19, 25]
M = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'), 
     ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'), 
     ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), 
     ('S', '...'), ('T', '-'), ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'), 
     ('Y', '-.--'), ('Z', '--..')]
print(titanic(W, M, D))"""