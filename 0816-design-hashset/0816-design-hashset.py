class MyHashSet:
    
    def __init__(self):
        self.lst=set({})

    def add(self, key: int) -> None:
        self.lst.add(key)

    def remove(self, key: int) -> None:
        if key in self.lst:
            self.lst.remove(key)
            return True
        return False
    def contains(self, key: int) -> bool:
        if key in self.lst:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)