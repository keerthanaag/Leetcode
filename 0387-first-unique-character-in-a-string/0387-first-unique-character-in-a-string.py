class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # lst=[]
        # lstdup=[]
        # pos=len(s)
        # for x in s:
        #     if x not in lst:
        #         lst.append(x)
        # for i in range(0,len(s)):
        #     for j in range(0,len(s)):
        #         if i!=j and s[i]==s[j]:
        #             lstdup.append(s[i])
        # temp=set(lst)-set(lstdup)
        # temp=list(temp)
        # if len(temp)==0:
        #     return -1
        # else:
        #     for x in temp:
        #         t=s.index(x)
        #         pos=min(pos,t)
        #     return pos 
        d={}
        lst=[]
        for x in s:
            if x not in d:
                d.update({x:1})
            else:
                val=d.get(x)
                val+=1
                d.update({x:val})
        print(d)
        for i,x in enumerate(s):
            if d.get(x)==1:
                return i
        return -1