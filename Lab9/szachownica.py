# Dana jest szachownica liczb wymmiernych n x n
# chcemy przejść z pola (1, 1) na pole (n, n)
# korzystając jedynie z ruchów: w dół, w prawo
# wejście na pole (i, j) kosztuje A[i][j]

# f(i, j) = min { f(i, j - 1), f(i - 1, j) } + A[i][j]
# f(0, 0) = A[0][0]