# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        after = curr.next
        curr.next = None

        while after:
            temp = after.next
            after.next = curr
            curr = after
            after = temp

        while head and curr:
            if head.val != curr.val:
                return False

            head = head.next
            curr = curr.next

        return True
            