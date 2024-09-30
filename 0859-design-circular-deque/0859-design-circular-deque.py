from collections import deque
class MyCircularDeque:

    def __init__(self, k: int):
        self.d=deque(maxlen=k)
        self.n=k
    def insertFront(self, value: int) -> bool:
        if len(self.d)<self.n:
            self.d.appendleft(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.d)<self.n:
            self.d.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.d)>0:
            self.d.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.d)>0:
            self.d.pop()
            return True
        return False

    def getFront(self) -> int:
        if len(self.d)>0:
            return self.d[0]
        else:
            return -1

    def getRear(self) -> int:
        if len(self.d)==0:
            return -1
        else:
            return self.d[len(self.d)-1]

    def isEmpty(self) -> bool:
        if len(self.d)==0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.d)==self.n:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()