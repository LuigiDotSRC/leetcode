from typing import List

# O(N) Time complexity, O(1) Space complexity
# Two pointers greedy approach to find the best local max
#   - move the bound with the lower value to attempt to find the next local max 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        l, r = 0, len(height) - 1

        while l < r:
            cur = min(height[l], height[r]) * (r - l)
            if cur > max: 
                max = cur
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return max


if __name__ == "__main__":
    sol = Solution()
    assert (sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49)
    assert (sol.maxArea([1,1]) == 1)
    assert (sol.maxArea([8,7,2,1]) == 7)
            
            
