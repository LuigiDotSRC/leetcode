from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         mstack = [(temperatures[-1], len(temperatures)-1)]
#         res = [0] * len(temperatures)
#         for i in range(len(temperatures)-2, -1, -1):
#             while len(mstack) > 0 and temperatures[i] > mstack[-1][0]: 
#                 mstack.pop()
#             if mstack:
#                 res[i] = mstack[-1][1] - i
#             mstack.append((temperatures[i], i))
            
#         return res