# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #we need to check the height
        """
        1. go all the way down
        2. get the combined diameter of the node height, to make it result
        3. then return the max height of either the left tree or right, + 1 for the height
        """
        res = 0
        def height(root):
            nonlocal res
            if root is None:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            res = max(res, left + right) #we want to get the max diameter

            return 1 + max(left, right) #we want the height of the subtree
        height(root)
        return res