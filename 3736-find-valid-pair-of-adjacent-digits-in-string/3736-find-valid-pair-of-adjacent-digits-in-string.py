class Solution:
    def findValidPair(self, s: str) -> str:
        d ={}
        for x in s:
            if x in d:
                val = d[x]
                val += 1
                d.update({x:val})
            else:
                d.update({x:1})
        print(d)
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                continue
            if int(s[i]) == d[s[i]] and int(s[i+1]) == d[s[i+1]]:
                return s[i:i+2]
        return ""        