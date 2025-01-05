from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pfx = 1
        for i in range(len(nums)):
            res[i] = pfx
            nums[i] *= nums[i]

        sfx = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= sfx
            sfx *= nums[i]

        return res