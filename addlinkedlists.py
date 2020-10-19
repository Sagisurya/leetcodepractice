class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode()
        x = l1.val + l2.val
        head.val = x%10
        carry = x//10
        current = head
        current1 = l1.next
        current2 = l2.next
        
        while current1 is not None or current2 is not None:
            x1 = current1.val if current1 is not None else 0
            x2 = current2.val if current2 is not None else 0
            x = x1 + x2 + carry
            #print(x)
            new = ListNode()
            new.val = x%10
            carry = x//10
            current.next = new
            current = current.next
            current1 = current1.next if current1 is not None else None
            current2 = current2.next if current2 is not None else None
        
        if carry !=0:
            new = ListNode()
            new.val = 1
            current.next = new
        return head