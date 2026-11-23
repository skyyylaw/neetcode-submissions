# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            node = head
            length = 0
            while node:
                length += 1
                node = node.next
                
            return length
        
        n1 = reverse(l1)
        n2 = reverse(l2)

        newHead = l1 if n1 >= n2 else l2

        carry = 0
        node = newHead
        prev = None
        while node:
            sum_ = 0
            if l1: 
                sum_ += l1.val
                l1 = l1.next
            if l2:
                sum_ += l2.val
                l2 = l2.next
            node.val = (sum_ + carry) % 10
            carry = (sum_ + carry) // 10 
            prev = node
            node = node.next
        if carry:
            prev.next = ListNode(carry)
        
        return newHead


        