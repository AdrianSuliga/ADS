"""
sort linked list (solution with selection sort)
"""
# q = 12
# 12 -> 14 -> None
# r
# 
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    def genList():
        e5 = Node(1, None)
        e4 = Node(2, e5)
        e3 = Node(4, e4)
        e2 = Node(5, e3)
        e1 = Node(13, e2)
        e0 = Node(21, e1)
        return e0
    def sort_list(p, k):
        nNode = Node(None, p)
        p = nNode
        result = Node(None, None)
        s = result
        while p.next is not None:
            q = Node.find_min(p, k)
            result.next = q
            result = result.next
        return s.next
    def find_min(p, k):
        prev, it = p, 0
        p = p.next
        mini = p.val
        while it < k and p.next is not None:
            if p.next.val < mini:
                prev = p
                mini = p.next.val
            p = p.next
            it += 1
        buffor = prev.next
        prev.next = buffor.next
        return buffor
    def print_list(p):
        while p is not None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)
    
p = Node.genList()
p.print_list()
p = p.sort_list(7)
p.print_list()