# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = None
        
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
                
                newTail, newHead = h, t

                reverse(h, t)
                counter = 0
                h, t = None, None

                if not memo:
                    ans = newHead
                    memo = [newHead, newTail]
                else:
                    memo[1].next = newHead
                    memo = [newHead, newTail]

            node = temp
            counter += 1    

        if not t:
            if not ans:
                return head
            memo[1].next = h
        
        # for i in range(1, len(memo)):
        #     memo[i-1][1].next = memo[i][0]

        return ans
        

        
