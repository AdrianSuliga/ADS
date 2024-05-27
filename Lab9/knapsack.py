from random import randint

# f(i, b) - funkcja zwraca maksymalny zysk gdy rozważamy przedmioty [0, ..., i] i mamy pojemność b plecaka
# f(i, b) = max { f(i - 1, b), f(i - 1, b - w[i]) + p[i] }
#                     ^                        ^
#                     |   bierzemy przedmiot i, zmniejszamy sobie tym samym pojemność plecaka i zwiększamy zysk                     
#        nie bierzemy przedmiotu i

# f(0, b) = p[0] gdy b >= w[0]
# f(0, b) = p[0] gdy b < w[0]

def knapsack(Weight:list, Profit:list, SackCapacity:int) -> tuple:
    n = len(Weight)
    F = [[0 for _ in range(SackCapacity + 1)] for _ in range(n)]
    Parent = [[(None, None) for _ in range(SackCapacity + 1)] for _ in range(n)]

    for b in range(Weight[0], SackCapacity + 1):
        F[0][b] = Profit[0]

    for b in range(SackCapacity + 1):
        for i in range(1, n):
            F[i][b] = F[i - 1][b]
            Parent[i][b] = (i - 1, b)
            if b >= Weight[i] and F[i - 1][b - Weight[i]] + Profit[i] > F[i][b]: 
                F[i][b] = F[i - 1][b - Weight[i]] + Profit[i]
                Parent[i][b] = (i - 1, b - Weight[i])

    Result = []
    item = (n - 1, SackCapacity)
    for i in range(n - 1, 0, -1):
        if item[1] != Parent[item[0]][item[1]][1]:
            Result.append(item[0])
        if Parent[item[0]][item[1]] != (None, None):
            item = Parent[item[0]][item[1]]
        else: break

    if item[1] >= Weight[0]: 
        Result.append(0)    

    Result.reverse()
    return F[n - 1][B], Result

n = int(input("n = "))
W = [randint(1, 10) for _ in range(n)]
P = [randint(1, 100) for _ in range(n)]
B = randint(n, 4 * n)

print(W)
print(P)
print(B)
print()

R, result = knapsack(W, P, B)
print(R)
print(result)
