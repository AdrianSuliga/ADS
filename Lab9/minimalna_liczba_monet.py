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

M = [1, 3, 4, 5]
T = 7
print(min_money(M, T, {}))