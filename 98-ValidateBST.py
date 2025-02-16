from typing import Optional
from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(cur, lmin=-float('inf'), lmax=float('inf')):
            if not cur:
                return True
            
            if cur.val <= lmin or cur.val >= lmax:
                return False

            l = dfs(cur.left, lmin, cur.val)
            r = dfs(cur.right, cur.val, lmax)

            return l and r

        return dfs(root)