class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss=(s+s)[1:-1]
        #[1:-1] slices this doubled string, removing the first and last characters. This effectively removes the first character of s and the last character of s from ss
        return s in ss
        # if len(s)==1:
        #     return False
        # lst=[]
        # for x in s:
        #     lst.append(x)
        # lst=sorted(set(lst))
        # temp="".join(lst)
        # if temp ==s:
        #     return True
        # elif len(s)%2 !=0:
        #     return False
        # else:
        #     mid=len(s)//2
        #     l=s[:mid]
        #     i=1
        #     n=len(l)
        #     while n<len(s):
        #         lg=l*i
        #         if lg==s:
        #             return True
        #         i+=1
        #         n=len(lg)
        #     return False