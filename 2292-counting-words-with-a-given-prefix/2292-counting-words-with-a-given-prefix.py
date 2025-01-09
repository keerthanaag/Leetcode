class Solution(object):
    def prefixCount(self, words, pref):
        count = 0
        n=len(pref)
        for x in words:
            if x[:n] == pref:
                count +=1
        return count
        