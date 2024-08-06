from collections import deque
class MinStack:
    
    def __init__(self):
        self.d=deque()
        self.flag=0
        self.n=len(self.d)
    def push(self, val: int) -> None:
        self.d.append(val)
        if self.flag==0:
            self.min_val=val
            self.flag=1
        else:
            self.min_val=min(val,self.min_val)
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