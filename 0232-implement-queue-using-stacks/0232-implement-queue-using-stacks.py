from collections import deque
class MyQueue:

    def __init__(self):
        self.d=deque()

    def push(self, x: int) -> None:
        self.d.append(x)
        for i in range(len(self.d)):
            self.d.append(self.d.popleft())

    def pop(self) -> int:
        return self.d.popleft()

    def peek(self) -> int:
        return self.d[0]

    def empty(self) -> bool:
        if len(self.d)==0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()