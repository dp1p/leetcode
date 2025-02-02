# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class LinkedList: 
#     def __init__(self, head=None):
#         self.head = head
    
#     def insert(self, value):
#         node = ListNode(value)
#         if self.head == None:
#             self.head = node
#             return
#         currentNode = self.head
#         while True:
#             if currentNode.next is None:
#                 currentNode.next = node
#                 return
#             currentNode = currentNode.next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        currentNode = head
        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        head = prevNode
        return head