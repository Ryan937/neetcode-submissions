# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = ListNode(0, head)
        slow, fast = result, head

        while n > 0:
            fast = fast.next
            n -= 1
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        temp = slow.next.next
        slow.next = None
        slow.next = temp

        return result.next