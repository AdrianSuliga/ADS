from zad11ktesty import runtests

# Adrian Suliga
# Algorytm oblicza wartość funkcji f takiej że:
# f(i, lsum, psum) - minimalna ilość odważników potrzebna gdy pewne jest że na lewym pokładzie jest lsum a na prawym psum
# f(i, lsum, psum) = min { f(i + 1, lsum + T[i], psum), f(i + 1, lsum, psum + T[i]) }
# przy czym znane i i lsum jednoznczanie określają psum, więc w celu przyspieszenia obliczeń
# wystarczy że funkcja zapamiętuje wartości f w tablicy o w wymiarach T na n gdzie T to suma 
# wszystkich kontenerowców. Szacuję złożoność czasową i pamięciową algorytmu na O(nT)

def kontenerowiec(T):
    n, sum = len(T), calc_sum(T)
    F = [[-1 for _ in range(sum + 1)] for _ in range(n)]
    return f(0, T, n, 0, 0, F)
    
def calc_sum(T):
    sum = 0
    for t in T: sum += t
    return sum

def f(i, T, n, left, right, F):
    if i == n: return abs(left - right)
    if F[i][left] != -1: return F[i][left]

    result = min(f(i + 1, T, n, left + T[i], right, F), f(i + 1, T, n, left, right + T[i], F)) 
    F[i][left] = result
    return result

runtests ( kontenerowiec )
#T = [1, 6, 5, 11]
#print(kontenerowiec(T))