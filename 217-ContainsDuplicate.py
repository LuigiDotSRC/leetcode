from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for n in nums: # O(N) worst scenario
            if n in visited: # O(1) lookup/add/delete
                return True
            visited.add(n)

        return False