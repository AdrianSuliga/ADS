from kol2testy import runtests
from queue import PriorityQueue

# Adrian Suliga
# Algorytm najpierw przepisuje graf G na listę krawędzi. Następnie oblicza optymalny czas dotarcia do każdego wierzchołka jeżeli wojownik jechał wcześniej
# przez j godzin gdzie 0 <= j <= 16. Optymalne czasy dotarcia zapisywane są w tablicy d[wierzchołek][czas], do ich policzenia wykorzystuję algorytm Dijkstry z 
# pewnymi modyfikacjami. Złożoność czasową algorytmu szacuję na O(ElogV), a pamięciową na O(E + V).

def warrior( G, s, t):
	G = list_form(G)
	n = len(G)
	d = [[float('inf') for _ in range(17)] for _ in range(n)] # d[i][j] to optymalny czas dotarcia do wierzchołka i, jeżeli wojownik ostatni raz spał j godzin temu
	Q = PriorityQueue()

	d[s][0] = 0 # do kolejki wrzucamy krotki w postaci:
	Q.put((d[s][0], 0, s)) # (optymalny koszt dotarcia do wierzchołka przy danej liczbie godzin od ostatniego postoju, liczba godzin od ostatniego postoju, wierzchołek)

	while not Q.empty():
		_, hours, u = Q.get()
		for v, cost in G[u]:
			if hours + cost <= 16 and d[u][hours] + cost < d[v][hours + cost]: # sytuacja gdy jedziemy z u do v bez spania
				d[v][hours + cost] = d[u][hours] + cost
				Q.put((d[v][hours + cost], hours + cost, v))
			if d[u][hours] + cost + 8 < d[v][cost]: # sytuacja gdy śpimy w u i jedziemy do v (dlatego w d[v][] porównujemy tylko cost, a nie cost + hours + 8)
				d[v][cost] = d[u][hours] + cost + 8
				Q.put((d[v][cost], cost, v))
			
	return min(d[t])

def list_form(E:list) -> list:
	n = 0
	for edge in E: n = max(n, edge[0], edge[1])

	G = [[] for _ in range(n + 1)]

	for edge in E:
		G[edge[0]].append((edge[1], edge[2]))
		G[edge[1]].append((edge[0], edge[2]))
	
	return G

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )