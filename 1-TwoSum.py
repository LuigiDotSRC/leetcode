from typing import List

# dictionary as element-index lookup
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()
        for i in range(len(nums)): # O(N) worst case
            req = target - nums[i]
            if req in visited:
                return [visited[req], i]
            visited[nums[i]] = i