from zad9ktesty import runtests
from math import inf

# Adrian Suliga
# f(i, g, d) - ilość aut na promie gdy rozważamy auta od 0. do i. przy długości pokładu górnego g, a dolnego d
# f(i, g, d) = max { f(i + 1, g + P[i], d), f(i + 1, g, d + P[i]) } + 1; g + P[i] <= g_max, d + P[i] <= d_max
# f(i, g, d) = 0 dla g > g_max lub d > d_max
# Szacuję złożoność czasową i pamięciową algorytmu na O(ngd)

def prom(P, g, d):
    n = len(P)
    Bottom_Cars, Top_Cars = [], []
    Index, Top_Capacity, Bottom_Capacity = 0, g, d
    F = [[[-1 for _ in range(d + 1)] for _ in range(g + 1)] for _ in range(n)]
    Max_Number_Of_Cars = f(0, g, d, P, F)    

    while Index < Max_Number_Of_Cars and (P[Index] <= Top_Capacity or P[Index] <= Bottom_Capacity):
        Choose_Top, Choose_Bottom = 0, 0

        if P[Index] > Top_Capacity:
            Choose_Top = 0
            Choose_Bottom = 1
        elif P[Index] > Bottom_Capacity:
            Choose_Top = 1
            Choose_Bottom = 0
        else:
            Choose_Top = F[Index + 1][Top_Capacity - P[Index]][Bottom_Capacity]
            Choose_Bottom = F[Index + 1][Top_Capacity][Bottom_Capacity - P[Index]]

        if Choose_Top > Choose_Bottom:
            Top_Cars.append(Index)
            Top_Capacity -= P[Index]
        else:
            Bottom_Cars.append(Index)
            Bottom_Capacity -= P[Index]
        
        Index += 1

    if Max_Number_Of_Cars - 1 in Top_Cars: return Top_Cars
    else: return Bottom_Cars

def f(i, g, d, P, F):
    if i > len(P) - 1: return 0

    if F[i][g][d] != -1:
        return F[i][g][d]

    if P[i] > g and P[i] > d:
        F[i][g][d] = 0
        return 0

    if P[i] > g:
        F[i][g][d] = f(i + 1, g, d - P[i], P, F) + 1
    elif P[i] > d:
        F[i][g][d] = f(i + 1, g - P[i], d, P, F) + 1
    else:
        top = f(i + 1, g - P[i], d, P, F)
        bottom = f(i + 1, g, d - P[i], P, F)
        F[i][g][d] = max(top, bottom) + 1
    
    return F[i][g][d]

runtests ( prom )
