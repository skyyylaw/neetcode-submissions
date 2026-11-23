# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        target = length - n + 1
        counter = 0
        node = head
        prev = None
        while node:
            counter += 1
            next = node.next
            if counter == target:
                if prev:
                    prev.next = next
                    node.next = None
                    return head
                else:
                    node.next = None
                    return next if next else None
            prev = node
            node = node.next

