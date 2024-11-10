class Solution:
    def isValid(self, word: str) -> bool:
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        if len(word) < 3:
            return False
        else:
            HasVowel = 0
            HasConsonant = 0
            for x in word:
                if x.isalnum() == False:
                    return False
                if x.isalpha() == True:
                    if x in vowel:
                        HasVowel = 1
                    else :
                        HasConsonant = 1
        if HasVowel == 1 and HasConsonant == 1:
            return True
        return False
