class Solution:
    def isPrefixAndSuffix(self,check : str,word:str) -> bool:
        lc = len(check)
        if check == word[:lc]:
            if check == word[-lc:]:
                return True
        return False
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count =0
        for i in range(len(words)):
            for j in range (i+1,len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]) == True:
                    count +=1
        return count
        