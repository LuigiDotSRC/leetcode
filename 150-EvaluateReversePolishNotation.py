from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t in set(['+','-','*','/']):
                e1 = stack.pop()
                e2 = stack.pop()
                match t:
                    case '+':
                        stack.append(e1 + e2)
                    case '-':
                        stack.append(e2 - e1)
                    case '*':
                        stack.append(e1 * e2)
                    case '/':
                        stack.append(int(float(e2)/e1))
            else:
                stack.append(int(t))

        return stack[0]
