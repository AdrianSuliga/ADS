# offline 1 attempt with O(V*E) time complexity
def Flight(L, x, y, t):
    G = rewrite_to_lists(L)
    V = len(G)
    visited = [False for _ in range(V)]
    d = [(0, float('inf')) for _ in range(V)]
    
    for u in G[x]: # for every point connected to x
        if not visited[u[0]]:
            if DFSvisit(G, x, u[0], u[1], visited, d, y, t):
                return True
    return False

def DFSvisit(G, parent, v, cost, visited, d, y, t):
    visited[v] = True
    d[v] = common_part(d[parent], (cost - t, cost + t))

    if d[v] == None:
        d[v] = (0, float('inf'))
        visited[v] = False
        return False
    
    if v == y: return True

    for u in G[v]:
        if not visited[u[0]]:
            if DFSvisit(G, v, u[0], u[1], visited, d, y, t):
                return True
    
    d[v] = (0, float('inf'))
    visited[v] = False
    return False

def common_part(t1, t2):
	if t1[0] <= t2[0] and t1[1] >= t2[1]: return t2
	if t2[0] <= t1[0] and t2[1] >= t1[1]: return t1
	if t2[0] <= t1[0] <= t2[1] <= t1[1]: return (t1[0], t2[1])
	if t1[0] <= t2[0] <= t1[1] <= t2[1]: return (t2[0], t1[1])
	return None

def rewrite_to_lists(L): # O(V + E)
    V = size_of_graph(L)
    G = [[] for _ in range(V)]
    for edge in L:
        G[edge[0]].append((edge[1], edge[2]))
        G[edge[1]].append((edge[0], edge[2]))
    return G

def size_of_graph(L):
    result = -1
    for edge in L:
        result = max(edge[0], edge[1], result)
    return result + 1

L = [(0,1,2000),(0,2,2100),(1,3,2050),(2,3,2300),
(2,5,2300),(3,4,2400),(3,5,1990),(4,6,2500),(5,6,2100)]
print(Flight(L, 0, 6, 50))