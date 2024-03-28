class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    def print_list(p):
        while p != None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)

    def get_middle(p):
        if p == None or p.next == None:
            return p
        slow, fast = p, p.next
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
        
        if p != None:
            result.next = p
        elif q != None:
            result.next = q

        buffor = start.next
        start.next = None
        return buffor

    def gen_list():
        e4 = Node(0, None)
        e3 = Node(4, e4)
        e2 = Node(3, e3)
        e1 = Node(5, e2)
        e0 = Node(-1, e1)
        return e0
    def merge_sort(p):
        if p == None or p.next == None:
            return p
        pivot = Node.get_middle(p)
        l1 = p
        l2 = pivot.next
        pivot.next = None
        l1 = Node.merge_sort(l1)
        l2 = Node.merge_sort(l2)
        return Node.merge(l1, l2)

p = Node.gen_list()
p.print_list()
p = p.merge_sort()
p.print_list()