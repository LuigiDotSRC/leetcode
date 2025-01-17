from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         stack = [(0, heights[0])]
#         ma = heights[0]
#         for i in range(1, len(heights)):
#             if len(stack) > 0 and heights[i] < stack[-1][1]:
#                 while len(stack) > 0 and heights[i] < stack[-1][1]:
#                     if (i - stack[-1][0]) * stack[-1][1] > ma:
#                         ma = (i - stack[-1][0]) * stack[-1][1]
#                     lp = stack.pop()
#                 stack.append((lp[0], heights[i]))
#             else:
#                 stack.append((i, heights[i]))

#         while stack:
#             c = stack.pop()
#             if (len(stack) - c[0]) * c[1] > ma:
#                 ma = (len(stack) - c[0]) * c[1]


#         return ma 

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         stack = [heights[0]]
#         ma = heights[0]
#         for i in range(1, len(heights)):
#             # print(i, stack, ma)
#             if len(stack) > 0 and heights[i] > stack[-1]:
#                 if stack[-1] * (len(stack) + 1) > ma:
#                     ma = stack[-1] * (len(stack) + 1)
#                 stack = []
            
#             stack.append(heights[i])
#             if stack[-1] * len(stack) > ma:
#                 ma = stack[-1] * len(stack)
        
#         # print(ma, stack)
#         return ma