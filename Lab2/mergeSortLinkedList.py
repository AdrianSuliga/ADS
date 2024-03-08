"""
posortować listę odsyłaczową poprzez wycinanie serii naturalnych (niemalejących podciągów)
"""
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def merge_lists(p, q):
        pass
    def extract_natural_sequence(p):
        start = p
        while p.next != None and p.val < p.next.val:
            p = p.next
        q = p.next
        p.next = None
        return (start, p, q)

    def gen_list(p):
        pass