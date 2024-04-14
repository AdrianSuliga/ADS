# sprawdź czy graf jest dwudzielny

# Odwiedzamy każdy wierzchołek i każdą krawędź, złożoność czasowa wynosi więc O(V + E), a pamięciowa O(V) - graf przechowywany za pomocą listy list
# Algorytm koloruje odwiedzone wierzchołki na dwa kolory: 1 lub -1, jeśli znajdziemy się w sytuacji że sąsiednie wierzchołki mają taki sam kolor
# to graf nie jest dwudzielny.

def is_bipartite(G):
    n = len(G)
    if n <= 1: return False
    Stack = []
    colors = [0 for _ in range(n)]
    for i in range(n): # iterujemy po wszystkich n wierzchołkach na wypadek gdyby graf nie był spójny
        if colors[i] == 0:
            Stack.append(i) # dodajemy na koniec stosu index wierzchołka od którego zaczynamy
            colors[i] = 1 # kolorujemy ów wierzchołek
            while len(Stack) > 0: # dopóki graf na którym jesteśmy jest spójny, to nie opuścimy tej pętli
                u = Stack.pop() # pobieramy wierzchołek ze stosu
                for v in G[u]: # iterujemy przez wszystkich jego sąsiadów
                    if colors[v] == 0: # jeżeli nie jest pokolorwany,
                        colors[v] = -1 * colors[u] # to kolorujemy na kolor przeciwny do poprzedniego wierzchołka
                        Stack.append(v) # dodajemy na stos aktualnie odwiedzanego sąsiada u
                    elif colors[v] == colors[u]: # jeżeli mają taki sam kolor to nie jest dwudzielny
                        return False
    return True

G = [
    [],
    [],
    [4, 5],
    [4, 5],
    [2, 3],
    [2, 3]
]
print(is_bipartite(G))