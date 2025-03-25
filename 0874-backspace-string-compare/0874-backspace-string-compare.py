class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = 0
        while i < len(s):
            print(i,s[i],s)
            if i == 0 and s[i] == '#':
                s = s[1:]
            elif s[i] == '#':
                s = s[:i-1]+s[i+1:]
                i -= 1
            else:
                i += 1
        print(s)
        i = 0
        while i < len(t):
            print(i,t[i],t)
            if i == 0 and t[i] == '#':
                t = t[1:]
            elif t[i] == '#':
                t = t[:i-1]+t[i+1:]
                i -= 1
            else:
                i += 1
        print(t)
        if s == t:
            return True
        else:
            return False
        