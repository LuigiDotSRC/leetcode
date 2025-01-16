from typing import List

# stack used as a string builder
# can always add an open parentheses as long as the count of open parentheses is less than n
# can always add a close parentheses as long as the count of close parentheses is less than open par
# prune paths that violate the rules, recursively explore all choices, store valid strings

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res