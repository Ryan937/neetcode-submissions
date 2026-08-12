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

        l1 = []
        l2 = []
        curr = head

        while slow:
            l1.append(curr.val)
            l2.append(slow.val)

            curr = curr.next
            slow = slow.next

        return l1 == l2[::-1]
