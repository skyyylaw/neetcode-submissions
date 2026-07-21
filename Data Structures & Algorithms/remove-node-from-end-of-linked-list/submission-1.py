# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m = 0
        node = head
        while node:
            m += 1
            node = node.next
        
        prev = None
        node = head

        if m == n:
            return head.next

        while m != n:
            m -= 1
            prev = node
            node = node.next
        
        if prev:
            prev.next = node.next
        
        node.next = None

        return head if node != head else None
        
        
