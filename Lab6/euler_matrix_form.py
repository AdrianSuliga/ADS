# find euler cycle in matrix represantation of graph
def euler_cycle(G, s):
    n = len(G)
    euler = []

    def euler_visit(G, u):
        for v in range(n):
            if G[u][v] > 0:
                G[u][v], G[v][u] = 0, 0
                euler_visit(G, v)
                euler.append(u)
    
    euler.append(s)
    euler_visit(G, s)

    return euler