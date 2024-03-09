"""
posortować listę odsyłaczową poprzez wycinanie serii naturalnych (niemalejących podciągów)
"""
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def print_list(p):
        while p != None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)

    def merge_lists(p, q):
        result = Node(None, None)
        start = result
        while p != None and q != None:
            if p.val <= q.val:
                result.next = p
                p = p.next
            else:
                result.next = q
                q = q.next
            result = result.next
        while p != None:
            result.next = p
            p = p.next
            result = result.next
        while q != None:
            result.next = q
            q = q.next
            result = result.next
        buffor = start.next
        start.next = None
        return buffor
    
    def sort_list(p):
        # ?

    def extract_natural_sequence(p):
        if p == None:
            return p
        start = p
        while p.next != None and p.val < p.next.val:
            p = p.next
        q = p.next
        p.next = None
        return (start, p, q)
    
    def gen_list():
        e10 = Node(14, None)
        e9 = Node(11, e10)
        e8 = Node(9, e9)
        e7 = Node(9, e8)
        e6 = Node(8, e7)
        e5 = Node(1, e6)
        e4 = Node(5, e5)
        e3 = Node(4, e4)
        e2 = Node(2, e3)
        e1 = Node(9, e2)
        e0 = Node(7, e1)
        return e0

p = Node.gen_list()
p.print_list()