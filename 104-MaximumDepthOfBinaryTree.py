from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(curr, depth=0):
            if not curr:
                return depth + 1
            
            left = dfs(curr.left, depth + 1)
            right = dfs(curr.right, depth + 1)

            if left > right:
                return left
            return right

        res = dfs(root)
        return res - 1