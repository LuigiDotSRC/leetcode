from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(target, s, e):
            if s > e:
                return -1

            mid = (s + e) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                return bs(target, s, mid-1)
            else:
                return bs(target, mid+1, e)
        
        return bs(target, 0, len(nums)-1)