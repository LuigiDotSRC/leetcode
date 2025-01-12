class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in set(['(','[','{']):
                stack.append(c)
            
            if c in set([')',']','}']):
                top = stack.pop()    

            match c:
                case ')':
                    if len(stack) == 0 or stack.pop() != '(':
                        return False
                case ']':
                    if len(stack) == 0 or stack.pop() != '[':
                        return False
                case '}':
                    if len(stack) == 0 or stack.pop() != '{':
                        return False
        
        if len(stack) != 0:
            return False
        return True