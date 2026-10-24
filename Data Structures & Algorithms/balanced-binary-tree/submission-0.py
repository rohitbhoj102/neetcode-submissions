# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return True, 0

            left_ok, left_h = dfs(node.left)
            right_ok, right_h = dfs(node.right)

            balanced = left_ok and right_ok and abs(left_h - right_h) <= 1
            height = 1 + max(left_h, right_h)
            return balanced, height

        
        return dfs(root)[0]