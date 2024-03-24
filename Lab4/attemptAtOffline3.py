# O(n) solution

def dominance(P:list):
    n = len(P)
    prefix_x = [0 for _ in range(n)]
    prefix_y = [0 for _ in range(n)]

    max_dom = -float('inf')

    counting_sort_x(prefix_x, P)
    counting_sort_y(prefix_y, P)
    
    return max_dom

def counting_sort_x(prefix_x, P):
    n = len(P)
    C = [0 for _ in range(n)]

    for i in range(n): C[P[i][0] - 1] += 1
    for i in range(1, n): C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        prefix_x[C[P[i][0] - 1] - 1] = P[i][0]
        C[P[i][0] - 1] -= 1

def counting_sort_y(prefix_y, P):
    n = len(P)
    C = [0 for _ in range(n)]

    for i in range(n): C[P[i][1] - 1] += 1
    for i in range(1, n): C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        prefix_y[C[P[i][1] - 1] - 1] = P[i][1]
        C[P[i][1] - 1] -= 1

P = [(1, 3), (3, 4), (4, 2), (2, 2)]
print(dominance(P))