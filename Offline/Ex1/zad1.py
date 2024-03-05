from zad1testy import Node, runtests

def SortH(p,k):
    nNode = Node()
    nNode.next = p
    p = nNode
    result = Node()
    s = result
    while p.next is not None:
        q = extractSmallest(p, k)
        result.next = q
        result = result.next
    return s.next

def extractSmallest(p, k):
    prev, it = p, 0
    p = p.next
    mini = p.val
    while it < k and p.next is not None:
        if p.next.val < mini:
            prev = p
            mini = p.next.val
        p = p.next
        it += 1
    buffor = prev.next
    prev.next = buffor.next
    return buffor


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
