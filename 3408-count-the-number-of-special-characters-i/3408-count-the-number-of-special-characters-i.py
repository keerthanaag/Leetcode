class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=set(word)
        return sum(1 for x in s if x.islower() and x.upper() in s)

        