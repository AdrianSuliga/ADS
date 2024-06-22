from egzP2atesty import runtests 

# Adrian Suliga
# Algorytm sortuje tablicę studentów po ich wzrostach, następnie wstawia do pomocniczej
# tablicy te wartości z uwzględnieniem warunków ułożenia studentów na zdjęciu. Na koniec
# kopiujemy już dobrze ułożonych studentów do początkowej tablicy. Szacuję złożoność czasową
# algorytmu na O(nlogn), a pamięciową na O(n)

def zdjecie(T:list, m, k):
    n = len(T)
    heap_sort(T)
    B = [None for _ in range(n)] # tablica pomocnicza gdzie wpiszemy studentów z uwzględnieniem
    indx = 0 # warunków zdjęcia, czyli indeksujemy po kolumnach

    for i in range(m - 1, -1, -1): # zaczynamy wpisywanie do tablicy od ostatniego wiersza
        j = i
        for _ in range(k): # pierwsze k komórek jest w tablicy B oddalonych od siebie o m
            B[j] = T[indx] # więc zwiększamy j o m
            indx += 1
            j += m
        step = m - 1
        for _ in range(m - i - 1): # ostatnie m - i - 1 komórek każdego wiersza wymaga
            B[j] = T[indx] # innego zmieniania j
            indx += 1
            j += step
            step -= 1

    for i in range(n): T[i] = B[i] # kopia do orginalnej tablicy

    return None

def heap_sort(T):
    n = len(T)
    build_heap(T)
    for i in range(n - 1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, i, 0)

def build_heap(T):
    n = len(T)
    for i in range((n - 1) // 2, -1, -1):
        heapify(T, n, i)

def heapify(T, n, i):
    l, r, mi = 2 * i + 1, 2 * i + 2, i
    if l < n and T[l][1] > T[mi][1]: mi = l
    if r < n and T[r][1] > T[mi][1]: mi = r
    if mi != i:
        T[mi], T[i] = T[i], T[mi]
        heapify(T, n, mi)

runtests ( zdjecie, all_tests=True )