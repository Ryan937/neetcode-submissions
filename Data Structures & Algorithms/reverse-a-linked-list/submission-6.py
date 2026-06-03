# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head

        curr = head
        next_node = head.next
        curr.next = None

        while next_node:
            temp = next_node.next
            next_node.next = curr
            curr = next_node
            next_node = temp

        return curr