from kol1testy import runtests

# Optimized n^2 solution

def maxrank(T):
	n = len(T)

	is_outranked = [False for _ in range(n)]

	max_rank = -1
	for i in range(n - 1, -1, -1):
		if is_outranked[i]: continue
		rank = 0
		for j in range(i):
			if T[j] < T[i]: 
				is_outranked[j] = True
				rank += 1
		max_rank = max(max_rank, rank)
		if max_rank > i: break
	return max_rank
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
