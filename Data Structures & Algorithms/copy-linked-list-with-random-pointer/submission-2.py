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

        nodes = dict()
        curr = head

        while curr:
            nodes[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            temp = nodes.get(curr)

            temp.next = nodes.get(curr.next)
            temp.random = nodes.get(curr.random)
            curr = curr.next

        return nodes.get(head)