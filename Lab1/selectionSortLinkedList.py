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
        e5 = Node(16, None)
        e4 = Node(12, e5)
        e3 = Node(14, e4)
        e2 = Node(5, e3)
        e1 = Node(3, e2)
        e0 = Node(21, e1)
        return e0
    def list_sort(p):
        result = None
        s = p
        p = Node(None, p)
        while p.next != None:
            q = Node.find_max(p)
            q.next = result
            result = q
        return s
    def find_max(p):
        maxi = 0
        while p.next != None:
            if p.next.val > maxi:
                mem = p
                maxi = p.next.val
            p = p.next
        result = mem.next
        mem.next = result.next
        return result
    def print_list(p):
        while p is not None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)
    
p = Node.genList()
p.print_list()
p.list_sort()
p.print_list()