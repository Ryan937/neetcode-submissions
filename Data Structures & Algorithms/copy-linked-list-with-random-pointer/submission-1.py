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

        my_dict = dict()
        curr = head

        while curr:
            my_dict[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            temp = my_dict[curr]

            temp.next = my_dict.get(curr.next)
            temp.random = my_dict.get(curr.random)
            curr = curr.next

        return my_dict[head]