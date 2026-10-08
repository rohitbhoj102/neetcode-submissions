# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # option 1: while loop
        # prev, curr = None, head

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp

        # return prev

        # option 2: recursion
        # base case
        if not head or not head.next:
            return head

        # recursive pattern
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

        