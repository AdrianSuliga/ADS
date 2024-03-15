def quick_sort(T):
    def sort(T, left, right):
        if left >= right: return
        pivot = partition(T, left, right)
        sort(T, left, pivot - 1)
        sort(T, pivot + 1, right)
    return sort(T, 0, len(T) - 1)
# stacks - size
def quick_sort_it(T):
    stack, n = [], len(T)
    stack.append((0, n - 1))
    while len(stack) > 0:
        p, r = stack.pop()
        pivot = partition(T, p, r)
        if p < pivot - 1: stack.append((p, pivot - 1))
        if pivot + 1 < r: stack.append((pivot + 1, r))

def partition(T, left, right):
    pivot = right
    index = left - 1
    for i in range(left, right):
        if T[i] < T[pivot]:
            index += 1
            T[i], T[index] = T[index], T[i]
    index += 1
    T[pivot], T[index] = T[index], T[pivot]
    return index

T = [9, 2, 5, 1, 19, 0, 5]
quick_sort_it(T)
print(T)