"""
Odwróć listę odsyłaczową
"""
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    def print_list(p):
        while p != None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)
    def gen_list():
        e3 = Node(6, None)
        e2 = Node(9, e3)
        e1 = Node(1, e2)
        e0 = Node(4, e1)
        return e0
    def reverse_rec(p):
        if p == None or p.next == None:
            return p
        q = Node.reverse_list(p.next)
        p.next.next = p
        p.next = None
        return q
    def reverse_list(p):
        if p == None or p.next == None:
            return p
        q = None
        f = p.next
        while f != None:
            p.next = q
            q = p
            p = f
            f = f.next
        p.next = q
        return p

p = Node.gen_list()
p.print_list()
p = p.reverse_rec()
p.print_list()