from random import randint
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def print_list(p):
        while p != None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)

    def gen_list(n):
        p = Node(None, None)
        start = p
        for _ in range(n):
            p.next = Node(randint(1,100), None)
            p = p.next
        buffor = start.next
        start.next = None
        return buffor
    
    def get_last(p):
        if p == None: return None
        while p.next != None:
            p = p.next
        return p
    
    def quick_sort(p):
        def sort(p, last):
            if p == None or p == last or p == last.next:
                return
            
            pivot_prev = Node.partition(p, last)
            sort(p, pivot_prev)

            if pivot_prev != None and pivot_prev == p:
                sort(pivot_prev.next, last)
            elif pivot_prev != None and pivot_prev.next != None:
                sort(pivot_prev.next.next, last)

        sort(p, p.get_last())
    
    def partition(head, last):
        if head == last or head == None or last == None:
            return head
        
        pivot_prev = head
        curr = head
        pivot = last.val

        while head != last:
            if head.val < pivot:
                pivot_prev = curr
                temp = curr.val
                curr.val = head.val
                head.val = temp
                curr = curr.next
            head = head.next
        
        temp = curr.val
        curr.val = pivot
        last.val = temp
        return pivot_prev


n = 10
p = Node.gen_list(n)
p.print_list()
p.quick_sort()
p.print_list()