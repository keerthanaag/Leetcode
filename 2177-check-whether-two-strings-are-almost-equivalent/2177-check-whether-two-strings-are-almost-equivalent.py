class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        s=set(word1).union(set(word2))
        for x in s:
            if abs(word1.count(x) - word2.count(x)) >3:
                return False
        return True
        
        