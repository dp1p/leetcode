# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        counter = 0
        # def dfs(root, counter):
        #     if root is None:
        #         return
            
        #     counter += 1
        #     if root.left:
        #         counter += 1
        #         dfs(root.left, counter)
        #     if root.right:
        #         counter += 1
        #         dfs(root.right, counter)
        if root is None:
            return 0
        stack = [root]
        
        while stack:
            counter += 1
            root = stack.pop()
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return (counter)
        # return counter
