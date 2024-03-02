"""
sort linked list (solution with selection sort)
"""
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
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