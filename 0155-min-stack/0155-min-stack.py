from collections import deque
class MinStack:
    
    def __init__(self):
        self.d=deque()
        self.n=len(self.d)

    def push(self, val: int) -> None:
        self.d.append(val)


    def pop(self) -> None:
        self.d.pop()

    def top(self) -> int:
        return self.d[self.n-1]

    def getMin(self) -> int:
        return min(self.d)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()