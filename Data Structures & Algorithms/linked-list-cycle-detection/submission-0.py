# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's Cycle Detection
        # initiate slow and fast pointer
        slow, fast = head, head

        # slow pointer moves one step
        # fast pointer moves two steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # if there is a cycle, 
                # the fast pointer will eventually lap the slow pointer
                return True

        return False