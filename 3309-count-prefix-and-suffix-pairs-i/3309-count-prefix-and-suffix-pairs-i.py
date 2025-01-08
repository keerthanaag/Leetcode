class Solution(object):
    def isPrefixAndSuffix(self,check,word):
        lc = len(check)
        if check == word[:lc]:
            if check == word[-lc:]:
                return True
        return False
    def countPrefixSuffixPairs(self, words):
        count =0
        for i in range(len(words)):
            for j in range (i+1,len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]) == True:
                    count +=1
        return count
        