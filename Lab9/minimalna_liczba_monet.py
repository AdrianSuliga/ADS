# M - tablica dostępnych monet, każdą możemy użyć wielokrotnie
# T - kwota do wydania
# Należy wydać kwotę T przy użyciu minimalnej ilości monet

# f(x, M) - minimalna liczba monet potrzebna do uzyskania sumy x gdy monety są ze zbioru M
# f(x, M) = min { f(x - t) + 1 | t w M i x >= t}
# f(0, M) = 0
# f(x, M) = +inf gdy x < 0

def min_money(M:list, x:int, memo:dict) -> int:
    if x in memo: return memo[x]
    if x == 0: return 0
    if x < 0: return float('inf')

    min_val = float('inf')

    for t in M:
        if x >= t:
            min_val = min(min_val, min_money(M, x - t, memo) + 1)

    memo[x] = min_val
    return memo[x]

def tab_min(M:list, x:int) -> int:
    F = [float('inf') for _ in range(x + 1)]

    F[0] = 0

    for target_num in range(1, x + 1):
        for coin in M:
            if target_num >= coin:
                F[target_num] = min(F[target_num], F[target_num - coin] + 1)

    return F[x]

M = [3, 4, 5]
T = 1
print(tab_min(M, T))