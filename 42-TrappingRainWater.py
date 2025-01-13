from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res, lmax, rmax = 0, 0, 0
        while l < r:
            if height[l] >= lmax:
                lmax = height[l]
            else:
                res += lmax - height[l]
            
            if height[r] >= rmax:
                rmax = height[r]
            else:
                res += rmax - height[r]
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return res