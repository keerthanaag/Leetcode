class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        i = 0
        lst = []
        while i+k <= len(s):
            temp = s[i:i+k]
            lst.append(temp)
            i += k
        if i < len(s):
            temp = s[i:]
            cnt = k - len(temp)
            temp = temp+ (fill*cnt)
            lst.append(temp)
        print(lst)
        return lst
        