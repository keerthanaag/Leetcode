class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count=0
        n_s=len(s)
        n_t=len(t)
        # for i in range(0,n_s):
        #     for j in range(0,n_t):
        #         if s[i]==t[j]:
        #             count+=1
        # if count>=n_s:
        #     return True
        # else:
        #     return False
        i=0
        if n_s>n_t:
            return False
        elif n_s==0:
            return True
        for x in t:
            if s[i]==x:
                count+=1
                if count>=n_s:
                    return True
                i+=1
        return False

        