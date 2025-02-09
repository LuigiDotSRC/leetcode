from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(c1, c2):
            if not c1 and not c2:
                return True
            if (
                not c1 and c2 or
                not c2 and c1 or
                c1.val != c2.val
            ):
                return False
            
            left = dfs(c1.left, c2.left)
            right = dfs(c1.right, c2.right)

            return left and right
        
        return dfs(p, q)