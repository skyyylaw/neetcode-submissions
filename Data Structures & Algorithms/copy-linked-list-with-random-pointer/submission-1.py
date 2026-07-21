"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        originalMemo = []
        originalIndex = dict()

        newMemo = []
        newIndex = dict()
        
        i = 0
        originalNode = head
        newNode = None
        while originalNode:
            originalMemo.append(originalNode)
            originalIndex[originalNode] = i

            newNextNode = Node(originalNode.val)
            
            if newNode:
                newNode.next = newNextNode
            newNode = newNextNode

            newMemo.append(newNode)
            newIndex[newNode] = i
            
            originalNode = originalNode.next

            i += 1
        
        for i, node in enumerate(originalMemo):
            if node.random:
                randomIndex = originalIndex[node.random]
                newMemo[i].random = newMemo[randomIndex]
        
        return newMemo[0]
        


                