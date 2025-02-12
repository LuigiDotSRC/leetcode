from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([(root, 0)])
        res = []
        level = []
        levelidx = 0

        while queue:
            cur = queue.popleft()
            
            if cur[0].left:
                queue.append((cur[0].left, cur[1]+1))
            if cur[0].right:
                queue.append((cur[0].right, cur[1]+1))

            if levelidx != cur[1]:
                levelidx = cur[1]
                res.append(level)
                level = [cur[0].val]
            else:
                level.append(cur[0].val)
        
        if len(level) > 0:
            res.append(level)
        return res