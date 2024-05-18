# Graf jest skierowany, reprezentowany macierzowo
# sprawdź czy ma uniwersalne ujście - wierzchołek do którego skierowany jest
# każdy inny wierzchołek, a który nie jest skierowany nigdzie

# Idziemy po przekątnej i sprawdzamy czy dany wierzchołek jest uniwersalnym ujściem, w najgorszym przypadku przejdziemy przez 2V
# komórek macierzy dla każdego elementu na przekątnej. Owych elementów jest V, zatem złożoność czasowa rozwiązania to O(2*V^2) czyli O(V^2)
def universal_mouth_brute(G):
    n = len(G)
    for i in range(n):
        is_mouth = True
        for j in range(n):
            if G[i][j] != 0: is_mouth = False
            if G[j][i] != 1 and i != j: is_mouth = False
        if is_mouth: return i
    return None

# Idziemy od komórki (0,0) zgodnie z regułami: jeśli 0 -> idziemy w prawo, jeśli 1 - idziemy w dół
# w ten sposób jeśli wyjdziemy poza tablicą to wiersz w którym wyjdziemy będzie odpowiadał potencjalnemu
# uniwersalnemu wyjściu. Jest to jedyny kandydat, jeśli on nie będzie wyjściem to nie ma wyjścia.
# Iterujemy się w najgorszym wypadku raz przez wszystkie wierzchołki, złożoność to więc O(V).
def universal_mouth_optimal(G):
    n = len(G)
    i, j = 0, 0
    while j < n and i < n:
        if G[i][j] == 0: j += 1
        elif G[i][j] == 1: i += 1
    
    for k in range(n):
        if G[i][k] != 0: return None
        if G[k][i] != 1 and k != i: return None
    return i

G = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0]
]

print(universal_mouth_brute(G))
print(universal_mouth_optimal(G))