# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #we can use a fast and slow pointer
        slow = head
        fast = head
        while slow and fast and fast.next: #while they are not none
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
