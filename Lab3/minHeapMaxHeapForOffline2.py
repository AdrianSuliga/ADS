# Program na początku sortuje pierwszy przedział [0 ... p - 1]
# następnie wrzuca k największych liczb z tego przedziału to min_heapa
# a resztę do max_heapa. W korzeniu min_heapa jest na początku k. największy
# element z [0 ... p - 1]. Nastęonie sprawdzamy co się stanie gdy ruszymy okno o 1.
# Badamy w szczególności czy element, który wyrzucamy z okna znajdował się w 
# min_heapie czy max_heapie?
# gdy był w min_heapie to wkładamy go to max_heapa, max_heapujemy i przekładamy do min_heapa max_heap[0]
# 
# gdy był w max_heapie to 

def ksum(T, k, p):
    
    return -1

def merge_sort(T):
    n = len(T)
    if n <= 1: return
    pivot = n // 2
    L = T[:pivot]
    R = T[pivot:]
    merge_sort(L)
    merge_sort(R)
    i, j, k = 0, 0, 0
    while i < pivot and j < n - pivot:
        if L[i] <= R[j]:
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