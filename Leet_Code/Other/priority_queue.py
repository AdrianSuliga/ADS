def left(i): return 2 * i + 1
def right(i): return 2 * i + 2
def parent(i): return (i - 1) // 2

def heapify(T, n, i):
    l, r, mi = left(i), right(i), i
    if l < n and T[l][1] > T[mi][1]: mi = l
    if r < n and T[r][1] > T[mi][1]: mi = r
    if mi != i:
        T[mi], T[i] = T[i], T[mi]
        heapify(T, n, mi)

def shift_up(T:list, i:int):
    while i > 0 and T[parent(i)][1] < T[i][1]:
        T[i], T[parent(i)] = T[parent(i)], T[i]
        i = parent(i)

def find_min(Queue:list, index:int):
    n = len(Queue)

    if left(index) > n - 1 and right(index) > n - 1:
        return (Queue[index][1], index)
    
    if left(index) < n:
        element1 = find_min(Queue, left(index))
    if right(index) < n:
        element2 = find_min(Queue, right(index))
        
    if element1[0] < element2[0]:
        return element1
    else:
        return element2

def enqueue(T:list, val:int, priority:int, size:int): # inserts elements into queue
    n = len(T)
    if len(T) + 1 > size:
        ind = find_min(T, 0)[1]
        T[ind], T[-1] = T[-1], T[ind]
        T.pop()
        T.append((val, priority))
        shift_up(T, n - 1)
    else:
        element = val, priority
        T.append(element)
        n += 1
        shift_up(T, n - 1)

def dequeue(T:list): # pops element with highest priority
    T[0], T[-1] = T[-1], T[0]
    T.pop()
    heapify(T, len(T), 0)

def main():
    size = 5
    Queue = []
    enqueue(Queue, 12, 7, size)
    enqueue(Queue, 2, 3, size)
    enqueue(Queue, 9, 1, size)
    enqueue(Queue, 7, 5, size)
    enqueue(Queue, 8, 10, size)
    print(Queue)
    enqueue(Queue, 4, 1, size)
    print(Queue)


if __name__ == "__main__":
    main()