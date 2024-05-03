class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        remnant = 0
        result = ListNode(None, None)
        start = result

        while l1 != None and l2 != None:
            result.next = ListNode((l1.val + l2.val + remnant) % 10, None)
            result = result.next
            remnant = (l1.val + l2.val + remnant) // 10
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            result.next = ListNode((l1.val + remnant) % 10, None)
            result = result.next
            remnant = (l1.val + remnant) // 10
            l1 = l1.next

        while l2 != None:
            result.next = ListNode((l2.val + remnant) % 10, None)
            result = result.next
            remnant = (l2.val + remnant) // 10
            l2 = l2.next

        if remnant != 0: result.next = ListNode(remnant, None)
        start = start.next
        return start