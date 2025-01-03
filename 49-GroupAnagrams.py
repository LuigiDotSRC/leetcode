from typing import List
from collections import defaultdict

# constrained input space: a-z

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # hash the list of letter frequencies
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s) # defaultdict creates a default value automatically

        return list(res.values())
