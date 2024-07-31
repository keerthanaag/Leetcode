class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n=len(needle)
        x=len(haystack)-(n-1)
        for i in range(0,x):
            l=haystack[i:n]
            n+=1
            if(needle==l):
                return i
        return -1