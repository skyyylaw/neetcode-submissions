# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        length = 1
        node = head
        while node.next:
            node = node.next
            length += 1
        tail = node

        boundary = math.ceil(length / 2.0)
        # print(boundary)

        # reverse the second half
        nodeCounter = 0
        node = head
        prev = None
        while node:
            nodeCounter += 1
            nxt = node.next
            if nodeCounter > boundary:
                if nodeCounter == boundary + 1:
                    prev.next = None
                    node.next = None
                else:
                    node.next = prev
            prev = node
            node = nxt

        # node = head
        # while node:
        #     print(node.val)
        #     node = node.next
        # node = tail
        # while node:
        #     print(node.val)
        #     node = node.next
        # return

        forward = head
        backward = tail
        while forward and backward:
            forwardNext = forward.next
            backwardNxt = backward.next
            
            forward.next = backward
            backward.next = forwardNext

            forward = forwardNext
            backward = backwardNxt
        
        # node = head
        # while node:
        #     print(node.val)
        #     node = node.next









