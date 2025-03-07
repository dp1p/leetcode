# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #preorder traversal
        #check if p.val and q.val are equal
        #if they are equal, go to the next node for both of them
        #continue
        def preorder(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            
            
            
            return preorder(p.left, q.left) and preorder(p.right, q.right)
        
        return preorder(p, q)