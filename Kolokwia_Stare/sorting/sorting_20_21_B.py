# k-chaotyczna lista
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    def gen_list():
        T = [6, 2, 10, 29, 24, 31, 45, 36, 49, 52, 51, 53, 58, 56, 61, 72, 71, 75, 82, 79]
        result = Node(None, None)
        s = result
        for i in range(len(T)):
            result.next = Node(T[i], None)
            result = result.next
        buf = s.next
        s.next = None
        return buf
    def print_list(p):
        while p != None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)
    def SortH(p, k):
        guardian = Node(None, p)
        p = guardian
        result = Node(None, None)
        start = result
        while p.next != None:
            smallest = p.extract_smallest(k)
            result.next = smallest
            result = result.next
        return start.next
    def extract_smallest(p, k):
        prev = p
        p = p.next
        mini_val = p.val
        it = 0
        while it < k and p.next != None:
            if p.next.val < mini_val:
                prev = p
                mini_val = p.next.val
            p = p.next
            it += 1
        result = prev.next
        prev.next = result.next
        result.next = None
        return result

p = Node.gen_list()
p.print_list()
p = p.SortH(1)
p.print_list()