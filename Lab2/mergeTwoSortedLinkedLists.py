"""
p1, p2 - posortowane listy odsyłaczowe. scal je w 1 posortowaną listę
"""
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def merge_lists_it(p, q):
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
            result = result.next
            p = p.next
        while q != None:
            result.next = q
            result = result.next
            q = q.next
        
        buffer = start.next
        start.next = None

        return buffer
    
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
p.print_list()
q.print_list()
m = Node.merge_lists_it(p, q)
m.print_list()
