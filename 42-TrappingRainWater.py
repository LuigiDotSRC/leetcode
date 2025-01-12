from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res, max = 0, 0
        while l < r:
            pass