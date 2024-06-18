from random import randint
# Dane są ciecze c1, c2, ..., cn
# p(ci) - zysk z cieczy i
# v(ci) - objętość cieczy i
# Zmaksymalizować zysk przy objętości maksymalnej L

# Definiujemy opłacalność cieczy ci jako p(ci) / v(ci)
# sortujemy ciecze po ich opłacalności, lejemy najbardziej
# opłacalną do wyczerpania, potem następną aż do zapełnienia L
# Nie jest poprawne ale good enoguh

def plecak(P, V, L):
    n, result = len(V), 0
    Z = [(P[i] / V[i], i) for i in range(n)]
    
    Z.sort(reverse = True)
    print(Z)
    index = 0

    while True:
        if L - V[Z[index][1]] >= 0:
            result += P[Z[index][1]]
            index += 1
            L -= V[Z[index][1]]
        else:
            break
    
    return result

n = 10
P = [randint(1, 10) for _ in range(n)]
V = [randint(1, 20) for _ in range(n)]
L = 50
print("P: ", P)
print("V: ", V)
print("L: ", L)
print(plecak(P, V, L))