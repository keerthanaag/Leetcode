class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        s=set(word)
        for x in s:
            if x.islower() and x.upper() in s:
                count+=1
        return count
        