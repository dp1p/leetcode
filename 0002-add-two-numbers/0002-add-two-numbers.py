# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #instantiate a new linkedlist as we will merge them
        #once it is instantiated it, continue the loop through l1 and l2
        #but if we have a carry, we must add it
        #once we add the vals of l1 and l2 and carry (if we have any)
        #add them val3
        dummy = ListNode()
        currentNode = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val3 = val2 + val1 + carry
            carry = val3 // 10 # get the remainder
            new_digit = val3 % 10 # get the last digit

            currentNode.next = ListNode(new_digit)
            currentNode = currentNode.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
            
        return dummy.next