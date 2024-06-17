from zad9testy import runtests
from math import inf

# Adrian Suliga
# Algorytm oblicza wartości następującej funkcji za pomocą rekurencji ze spamiętywaniem
# f(i, j) - najdłuższa ścieżka wychodząca z góry M[i][j]
# zauważmy że f(i, j) = max { f(i - 1, j), f(i + 1, j), f(i, j - 1), f(i, j + 1) }
# Ale możemy przejść do innej góry tylko gdy jest ona wyżej i gdy nie wyjdziemy indeksami poza tablicę
# Szacuję złożoność czasową i pamieciową algorytmu na O(mn)

def trip(M):
	m, n = len(M), len(M[0])
	F = [[0 for _ in range(n)] for _ in range(m)] # Tablica na wartości funkcji f(i, j)

	for i in range(m):
		for j in range(n):
			if F[i][j] == 0: # Dzięki temu warunkowi nie będziemy obliczać żadnych ścieżek 2 razy przez co złożoność 
				F[i][j] = travel(i, j, M, m, n, F) # czasowa wyniesie O(mn)

	result = -1
	for i in range(m):
		for j in range(n):
			result = max(result, F[i][j])
	return result
	
def travel(i, j, M, m, n, F):
	if F[i][j] != 0: return F[i][j] # jeśli znamy już najdłuższą ścieżkę z danego wierzchołka to nie
	if -1 < i < m and -1 < j < n: # ma po co liczyć dalej
		result = 1
		if i + 1 < m and M[i][j] < M[i + 1][j]:
			result = max(result, travel(i + 1, j, M, m, n, F) + 1)
		if -1 < i - 1 and M[i][j] < M[i - 1][j]:
			result = max(result, travel(i - 1, j, M, m, n, F) + 1)
		if j + 1 < n and M[i][j] < M[i][j + 1]:
			result = max(result, travel(i, j + 1, M, m, n, F) + 1)
		if -1 < j - 1 and M[i][j] < M[i][j - 1]:
			result = max(result, travel(i, j - 1, M, m, n, F) + 1)
		F[i][j] = result # spamiętujemy wynik
		return result
	else:
		return -inf

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )
