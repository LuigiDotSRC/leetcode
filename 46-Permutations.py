from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(cur, rem):
            nonlocal res
            if not rem:
                res.append(cur)
                return
             
            for i in range(len(rem)):
                cur.append(rem[i])
                dfs(cur, rem[0:i]+rem[i+1:len(rem)])
                cur.pop()    

        dfs([], nums)
        return res
    
