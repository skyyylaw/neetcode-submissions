# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, tail):
            prev = None
            curr = head
            while prev != tail:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

        memo = []

        node = head
        counter = 1
        h, t = None, None

        while node:
            # print(node.val, counter)
            temp = node.next
            if counter == 1:
                h = node
            elif counter == k:
                t = node
                memo.append((t, h))
                reverse(h, t)
                counter = 0
                h, t = None, None
            node = temp
            counter += 1    
        
        if not t:
            memo.append((h, t))
        
        for i in range(1, len(memo)):
            memo[i-1][1].next = memo[i][0]

        return memo[0][0]
        

        
