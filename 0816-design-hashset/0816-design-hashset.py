class MyHashSet(object):

    def __init__(self):
        self.st=set({})

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.st.add(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.st:
            self.st.remove(key)
            return True
        return False
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.st:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)