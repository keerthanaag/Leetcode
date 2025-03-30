class Solution(object):
    def getEncryptedString(self, s, k):
        i = 0
        temp = []
        while i < len(s):  
            pos = (i+k)  % len(s)
            temp.append(s[pos])
            i += 1
        return "".join(temp)