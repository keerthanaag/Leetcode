class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        else:
            d={}
            l={}
            for i in range(len(s)):
                d.update({s[i]:t[i]})
            for i in range(len(s)):
                l.update({t[i]:s[i]})
            temp1=''
            temp2=''
            #print(d)
            #print(l)
            for x in s:
                temp1+=d.get(x)
            #print(temp1,t)
            for x in t:
                temp2+=l.get(x)
            #print(temp2,s)
            
            if temp1 == t and temp2 == s:
                return True
            else:
                return False
        