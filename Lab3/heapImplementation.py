# implement inserting element into binary heap

# first element in array stores size of heap

def parent(i):
    return i // 2
def left(i):
    return 2 * i
def right(i):
    return 2 * i + 1    

def insert(T, v):
    i = T[0] + 1
    T[0] += 1
    j = parent(i)
    while i > 0 and v > T[j]:
        T[i] = T[j]
        i = j
        j = parent(i)
    T[i] = v
    return T
