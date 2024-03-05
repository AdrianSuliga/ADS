class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    def genList():
        e13 = Node(56, None)
        e12 = Node(58, e13)
        e11 = Node(53, e12)
        e10 = Node(51, e11)
        e9 = Node(52, e10)
        e8 = Node(49, e9)
        e7 = Node(36, e8)
        e6 = Node(45, e7)
        e5 = Node(31, e6)
        e4 = Node(24, e5)
        e3 = Node(29, e4)
        e2 = Node(10, e3)
        e1 = Node(2, e2)
        e0 = Node(6, e1)
        return e0
    
    def SortH(p,k):
        nNode = Node(None, p)
        p = nNode
        result = Node(None, None)
        s = result
        while p.next is not None:
            q = Node.extractSmallest(p, k)
            result.next = q
            result = result.next
        return s.next
    
    def extractSmallest(p, k):
        prev, it = p, 0
        p = p.next
        mini = p.val
        while p.next is not None and it < k:
            if p.next.val < mini:
                prev = p
                mini = p.next.val
            p = p.next
            it += 1
        buffor = prev.next
        prev.next = buffor.next
        return buffor
    
    def printList(p):
        while p is not None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)

p = Node.genList()
p.printList()
p = p.SortH(1)
p.printList()