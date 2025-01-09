from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort() # O(nlogn)
#         l, r = 0, len(nums) - 1
        
#         res = []
#         while l < r:
#             cur = nums[l] + nums[r]

#             # the value to sum to get 0 is within the l and r ptrs
#             if cur * -1 >= nums[l] and cur * -1 <= nums[r]:
#                 for i in range(l, r):
#                     if nums[i] + cur == 0:
#                         res.append([nums[l], nums[r], nums[i]])
#                         break

#                     # could not find value within the range
#                     if nums[i] > cur * -1:
#                         break

#             if cur > 0:
#                 prev = nums[r]
#                 # seek the next unique val
#                 while r > l and nums[r] == prev:
#                     r -= 1
#             else:
#                 prev = nums[l]
#                 while l < r and nums[l] == prev:
#                     l += 1
        
#         return res
