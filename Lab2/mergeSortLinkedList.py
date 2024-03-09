class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def print_list(p):
        while p != None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)

    def merge_sort(p):
        if p == None or p.next == None:
            return p
        pivot = Node.get_middle(p)
        l1 = p
        l2 = pivot.next
        pivot.next = None
        l1 = l1.merge_sort()
        l2 = l2.merge_sort()
        return Node.merge(l1, l2)

    def get_middle(p):
        if p == None or p.next == None:
            return p
        fast, slow = p.next, p
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(p, q):
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
    
    def gen_list():
        e6 = Node(5, None)
        e5 = Node(9, e6)
        e4 = Node(7, e5)
        e3 = Node(16, e4)
        e2 = Node(1, e3)
        e1 = Node(5, e2)
        e0 = Node(13, e1)
        return e0
    
p = Node.gen_list()
p.print_list()
p = p.merge_sort()
p.print_list()