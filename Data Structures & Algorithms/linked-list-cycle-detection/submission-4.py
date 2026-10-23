# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while slow != None:
            if slow:
                slow = slow.next
            if fast:
                fast = fast.next
            if fast:
                fast = fast.next
            if slow == fast and slow:
                return True
        return False
