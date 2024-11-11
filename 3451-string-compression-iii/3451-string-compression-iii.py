class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        i = 0
        n = len(word)
        
        while i < n:
            char = word[i]
            count = 1
            # Check up to 9 repetitions of the current character
            while i + 1 < n and word[i + 1] == char and count < 9:
                count += 1
                i += 1
            # Append compressed result for the current character
            ans += str(count) + char
            i += 1
        
        return ans
