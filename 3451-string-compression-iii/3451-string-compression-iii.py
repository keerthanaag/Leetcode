class Solution:
    def compressedString(self, word: str) -> str:
        charac = ''
        times = 0
        ans = ''
        for i in range(len(word)):
            if i == 0:
                charac = word[i]
                times += 1
            else:
                if charac == word[i] and times < 9:
                    times += 1
                else:
                    ans += str(times)+charac
                    times = 1
                    charac = word[i]
        ans += str(times)+charac
        return ans
        
