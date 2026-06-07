# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        curr = result
        carryover = 0

        while l1 and l2:
            added = l1.val + l2.val + carryover

            if added >= 10:
                added %= 10
                carryover = 1
            else:
                carryover = 0

            curr.next = ListNode(added)
            l1, l2, curr = l1.next, l2.next, curr.next

        temp = l1 if l1 else l2

        while temp:
            added = temp.val + carryover

            if added >= 10:
                added %= 10
                carryover = 1
            else:
                carryover = 0

            curr.next = ListNode(added)
            temp, curr = temp.next, curr.next

        if carryover == 1:
            curr.next = ListNode(1)

        return result.next