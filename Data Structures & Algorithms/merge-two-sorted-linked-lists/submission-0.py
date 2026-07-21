# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        node = head
        while list1 or list2:
            if list1 and (not list2 or list1.val <= list2.val):
                if not head:
                    head = list1
                    node = head
                else:
                    node.next = list1
                    node = node.next
                list1 = list1.next
            else:
                if not head:
                    head = list2
                    node = head
                else:
                    node.next = list2
                    node = node.next
                list2 = list2.next
        return head