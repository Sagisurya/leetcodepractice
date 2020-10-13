class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return
        
        while head.val == val:
            head = head.next
            if head is None:
                return
        curr = head
        
        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head