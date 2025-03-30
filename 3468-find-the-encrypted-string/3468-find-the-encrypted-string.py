class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        i = 0
        temp = []
        while i < len(s):  
            pos = (i+k)  % len(s)
            print(s[i],s[pos])
            temp.append(s[pos])
            i += 1
        print(temp)
        return "".join(temp)
                