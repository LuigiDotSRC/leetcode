from collections import set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l, maxL = 0, 0
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            maxL = max(maxL, r - l + 1)
        return maxL