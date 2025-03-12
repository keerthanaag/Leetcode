class Solution(object):
    def isPrefixString(self, s, words):
        temp = ""
        for x in words:
            temp += x
            n = len(s)
            if len(temp) > n:
                return False
            elif s == temp[:n]:
                return True
        return False
        