class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        flag=0
        n=len(s)
        m=len(t)
        if n == m:
            for i in range(0,n):
                a=s[i]
                if s.count(a)==t.count(a):
                    flag+=1
            if flag==n:
                return True
            else:
                return False
        else:
            return False

        