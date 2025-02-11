# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # find p and q, return the path taken to reach
        def dfs(cur, target, path=[]):
            if not cur:
                return None
            
            if cur.val == target.val:
                return path + [cur]
            
            left_path = dfs(cur.left, target, path + [cur])
            if left_path:
                return left_path
            
            right_path = dfs(cur.right, target, path + [cur])
            return right_path

        pathP = dfs(root, p)
        pathQ = dfs(root, q)

        i = 0
        res = None
        while i < min(len(pathP), len(pathQ)):
            if pathP[i] == pathQ[i]:
                res = pathP[i]
            i += 1 
        
        return res