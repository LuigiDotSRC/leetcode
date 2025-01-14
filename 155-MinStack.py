# keeping track of a current running minval by tagging it with stack node

class MinStack:

    def __init__(self):
        self.stack = [] # tuple(val, currentMinVal)

    def push(self, val: int) -> None:   
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))
    
    def pop(self) -> None:
        self.stack = self.stack[:len(self.stack)-1]
        # problem: keeping a recurrent minval tracker will break since we don't know the next min val after current is removed

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int: # O(1)
        return self.stack[-1][1]