class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    def insert(p, node):
        if p.next == None:
            p.next = node
            return p
        start, prev = p, p
        p = p.next
        while p != None:
            if p.val >= node.val and prev.val < node.val:
                break
            prev = p
            p = p.next
        prev.next = node
        node.next = p
        return start
    
    def insertion_sort(p):
        nNode = Node(None, p)
        p = nNode
        result = Node(-float('inf'), None)

        while p.next != None:
            to_insert = p.next
            p.next = to_insert.next
            to_insert.next = None
            result = Node.insert(result, to_insert)

        return result.next
    
    def print_list(p):
        while p != None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)

    def gen_list():
        e4 = Node(0, None)
        e3 = Node(4, e4)
        e2 = Node(3, e3)
        e1 = Node(5, e2)
        e0 = Node(-1, e1)
        return e0

p = Node.gen_list()
p.print_list()
p = p.insertion_sort()
p.print_list()