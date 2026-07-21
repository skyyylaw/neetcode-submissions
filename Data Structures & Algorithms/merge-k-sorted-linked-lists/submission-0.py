# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        prev = None
        while True:
            mini = None
            index = 0
            for i, node in enumerate(lists):
                if node and (not mini or mini.val > node.val):
                    index = i
                    mini = node
            
            if not mini:
                break
            
            lists[index] = lists[index].next

            if not head:
                head = mini
                prev = mini
            else:
                prev.next = mini
                prev = prev.next
                prev.next = None
        
        return head