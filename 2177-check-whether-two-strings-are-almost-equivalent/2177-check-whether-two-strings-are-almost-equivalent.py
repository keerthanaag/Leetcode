class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        s=set(word1).union(set(word2))
        for x in s:
            if abs(word1.count(x) - word2.count(x)) >3:
                return False
        return True
        
        