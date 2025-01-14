class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        lst = []
        for i in range(1,len(A)+1):
            s = set(A[:i]).intersection(set(B[:i]))
            lst.append(len(s))
        return lst
        