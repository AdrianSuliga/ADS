from egzP6atesty import runtests 

# Adrian Suliga
# Algorytm sortuje otrzymaną listę haseł po ich długości za pomocą algorytmu counting sort.
# Po takim posortowaniu możemy łatwo odczytać długość najsłabszego z silnych haseł, wynosi
# ona tyle samo co długość hasła H[s - 1]. 
# Dlaczego?
# Po posortowaniu haseł po długości (od największego do najmniejszego) nie są one jeszcze 
# posortowane po swojej sile. Pozostaje nam w ramach każdego fragmentu tablicy z napisami
# tej samej długości posortować ja po ilości liter, czyli odpowiedź do zadania na pewno będzie
# miała tą samą długość co napis znajdujący się w H[s - 1].
# Skoro znamy już długość szukanego napisu to pozostaje posortowanie tylko jednego fragmentu
# tablicy. Algorytm znajduje go w czasie O(n), a potem sortuje po ilości liter counting sortem
# Szacuję złożoność czasową algorytmu na O(nk), a pamięciową na O(n + k).

def google ( H, s ):
    n = len(H)
    L = [len(H[i]) for i in range(n)]

    counting_sort(H, L, n)
    start, end = 0, 0

    for i in range(n):
        if L[i] == L[s - 1]:
            start = i
            break
    
    for i in range(1, n):
        if L[i - 1] == L[s - 1] and L[i] != L[s - 1]:
            end = i
            break
    
    A = H[start : end]
    a = len(A)

    R = [0 for _ in range(a)]

    for i in range(a):
        for char in A[i]:
            if ord('a') <= ord(char) <= ord('z'):
                R[i] += 1
    
    counting_sort(A, R, a)

    return A[s - start - 1]

# nk sorting
def counting_sort(H:list, L:list, n:int) -> None:
    k = max_len(H)
    C = [0 for _ in range(k + 1)]
    B = [None for _ in range(n)]
    S = [None for _ in range(n)]

    for i in range(n): C[L[i]] += 1

    for i in range(1, k + 1): C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[L[i]] - 1] = L[i]
        S[C[L[i]] - 1] = H[i]
        C[L[i]] -= 1

    for i in range(n): 
        L[i] = B[i]
        H[i] = S[i]

    L.reverse()
    H.reverse()

def max_len(H:list) -> int:
    n = 0
    for s in H: n = max(n, len(s))
    return n

runtests ( google, all_tests=True )