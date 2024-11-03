class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        return sum(1 for x in set(word) if x.islower() and x.upper() in set(word))

        