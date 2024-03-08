"""
p1, p2 - posortowane listy odsyłaczowe. posortuj je
"""
# iteracyjnie: jak w merge sorcie
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def merge_lists_it(p, q):
        pass
    def merge_lists_rec(p, q):
        if p == None: return q
        if q == None: return p
        if p.val < q.val:
            p.next = Node.merge_lists_rec(p.next, q)
            return p
        q.next = Node.merge_lists_rec(p, q.next)
        return q
    def gen_p():
        e3 = Node(7)
        e2 = Node(5, e3)
        e1 = Node(3, e2)
        e0 = Node(2, e1)
        return e0
    def gen_q():
        e2 = Node(6)
        e1 = Node(4, e2)
        e0 = Node(1, e1)
        return e0
    def print_list(p):
        while p is not None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)

p = Node.gen_p()
q = Node.gen_q()
m = Node.merge_lists_rec(p, q)
m.print_list()
