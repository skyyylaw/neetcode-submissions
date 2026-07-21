# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list1 = head
        list2 = None
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        node = head
        for _ in range(n//2 - 1):
            node = node.next
        node.next, node = None, node.next
        list2 = node

        print(list1, list2)

        # reverse list2
        prev = None
        curr = list2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        list2 = prev


        ans = ListNode()
        node = ans
        while list1 or list2:
            if list1:
                node.next = list1
                list1 = list1.next
                node = node.next
            if list2:
                node.next = list2
                list2 = list2.next
                node = node.next
        
        head = ans
                

        

