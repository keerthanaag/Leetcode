class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        def check(s):
            lst=[]
            i=0
            temp=""
            flag=0
            while(i<len(s)):
                if s[i]=='A' and i<len(s)-1:
                    if s[i+1]=="B":
                        i=i+2
                        flag=1
                    else:
                        temp+=s[i]
                        i+=1
                elif s[i]=='C' and i<len(s)-1:
                    if s[i+1]=='D':
                        i=i+2
                        flag=1
                    else:
                        temp+=s[i]
                        i+=1
                else:
                    temp+=s[i]
                    i+=1
            lst.append(temp)
            lst.append(flag)
            return lst
        t=check(s)
        while(t[1]==1):
            t=check(t[0])
        return len(t[0])
        