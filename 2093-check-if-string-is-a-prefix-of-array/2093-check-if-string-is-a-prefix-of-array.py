class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        temp = ""
        for x in words:
            temp += x
            n = len(s)
            if len(temp) > n:
                return False
            elif s == temp[:n]:
                return True
        return False
        