class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        lst = []
        for i in range(len(s)-1):
            print(s[i:i+2])
            lst.append(s[i:i+2])
        rev = s[::-1]
        for i in range(len(rev)-1):
            temp = rev[i:i+2]
            if temp in lst:
                return True
        return False
        