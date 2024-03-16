# Program na początku sortuje pierwszy przedział [0 ... p - 1]
# następnie wrzuca k największych liczb z tego przedziału to min_heapa
# a resztę do max_heapa. W korzeniu min_heapa jest na początku k. największy
# element z [0 ... p - 1]. Następnie sprawdzamy co się stanie gdy ruszymy okno o 1.
# Badamy w szczególności czy element, który wyrzucamy z okna znajdował się w 
# min_heapie czy max_heapie?

# -Gdy był w min_heapie to nowy element, który uzyskujemy poprzez przesunięcie okna dodajemy do max_heapa, heapujemy
# go i największy element zawsze przekładamy do min_heapa. Po prostu skoro tracimy element z min_heapa to musimy dodać do niego jakiś
# nowy. Przy czym należy pamiętać że podczas ściągania min_heap[0] musimy sprawdzić czy nie jest on aby poza przedziałem, czy nie został stracony.
# w każdym innym przypadku elementami traconymi poprzez przesuwanie okna nie musimy się martwić - nie psują nam min_heapa

# -Gdy był w max_heapie to nowy element dokładamy do max_heapa, heapujemy i przekładamy do min_heapa TYLKO jeżeli max_heap[0] > min_heap[0]

# Jako że funkcje heapujące zamieniają kolejność elementów to w kopcach musimy przechowywać indeksy elementów w tablicy obok ich wartości,
# żeby wiedzieć które są a które nie są w rozważanym aktualnie przedziale.

from zad2testy import runtests
def ksum(T, k, p):
    n = len(T)

    spare_array = [(T[i], i) for i in range(p)]
    merge_sort_modified(spare_array)
    
    is_in_min_heap = [False for _ in range(n)]

    max_heap = spare_array[0:(p-k)]
    min_heap = spare_array[(p-k):p]
    for i in range(k):
        is_in_min_heap[min_heap[i][1]] = True

    build_heap(min_heap, True)
    build_heap(max_heap, False)

    return calc_sum(T, max_heap, min_heap, is_in_min_heap, (n, p))

def calc_sum(T:list, max_heap:list, min_heap:list, is_in_min_heap:list, bundle:tuple):
    sum = 0
    n, p = bundle
    for i in range(n - p + 1):
        while len(min_heap) > 0:
            kVal, kInd = min_heap[0]
            if i <= kInd <= i + p - 1: 
                break
            else:
                is_in_min_heap[kInd] = False
                heap_pop(min_heap, True)
        sum += kVal

        if is_in_min_heap[i] and i + p < n: # jeśli element tracony jest w min heapie i możemy przesunąć się dalej
            heap_insert(max_heap, T[i + p], i + p, False)
            while len(max_heap) > 0:
                mVal, mInd = max_heap[0]
                heap_pop(max_heap, False)
                is_in_min_heap[mInd] = False
                if i + 1 <= mInd <= i + p: break
            heap_insert(min_heap, mVal, mInd, True)
            is_in_min_heap[mInd] = True
        elif not is_in_min_heap[i] and i + p < n:
            heap_insert(max_heap, T[i + p], i + p, False)
            while max_heap[0][0] > min_heap[0][0]:
                if i + 1 <= max_heap[0][1] <= i + p:
                    is_in_min_heap[min_heap[0][1]] = False
                    is_in_min_heap[max_heap[0][1]] = True
                    min_heap[0], max_heap[0] = max_heap[0], min_heap[0]
                    heapify(min_heap, len(min_heap), 0, True)
                    heapify(max_heap, len(max_heap), 0, False)
                    break
                else:
                    heap_pop(max_heap, False)
    return sum

def heap_insert(heap:list, val, ind, heap_flag):
    heap.append((val, ind))
    pos = len(heap) - 1
    if heap_flag:
        while pos > 0 and heap[parent(pos)][0] > heap[pos][0]:
            heap[parent(pos)], heap[pos] = heap[pos], heap[parent(pos)]
            pos = parent(pos)
    else:
        while pos > 0 and heap[parent(pos)][0] < heap[pos][0]:
            heap[parent(pos)], heap[pos] = heap[pos], heap[parent(pos)]
            pos = parent(pos)

def heap_pop(heap:list, heap_flag): # remove first element and maintain heap structure (heapify broken element)
    heap[0], heap[-1] = heap[-1], heap[0]
    heap.pop()
    heapify(heap, len(heap), 0, heap_flag)

def build_heap(T, heap_flag): # if heap_flag: build min_heap
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i, heap_flag)

def heapify(T, n, i, heap_flag): # if heap_flag: build min_heap
    l, r = left(i), right(i)
    mi = i
    if heap_flag:
        if l < n and T[l][0] < T[mi][0]:
            mi = l
        if r < n and T[r][0] < T[mi][0]:
            mi = r
    else:
        if l < n and T[l][0] > T[mi][0]:
            mi = l
        if r < n and T[r][0] > T[mi][0]:
            mi = r
    if mi != i:
        T[mi], T[i] = T[i], T[mi]
        heapify(T, n, mi, heap_flag)

def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2
def parent(i):
    return (i - 1) // 2

def merge_sort_modified(T):
    n = len(T)
    if n <= 1: return
    pivot = n // 2
    L = T[:pivot]
    R = T[pivot:]
    merge_sort_modified(L)
    merge_sort_modified(R)
    i, j, k = 0, 0, 0
    while i < pivot and j < n - pivot:
        if L[i][0] <= R[j][0]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1
        k += 1
    while i < pivot:
        T[k] = L[i]
        i += 1
        k += 1
    while j < n - pivot:
        T[k] = R[j]
        j += 1
        k += 1
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
    