class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        lst=[]
        if len(s1)!=len(s2):
            return False
        if s1==s2:
            return True
        else:
            for i,x in enumerate(s1):
                if s1[i]!=s2[i] and i not in lst:
                    lst.append(i)
            if len(lst)!=2:
                return False
            else:
                lst=sorted(lst)
                temp=s2[:lst[0]]+s2[lst[1]]+s2[lst[0]+1:lst[1]]+s2[lst[0]]+s2[lst[1]+1:]
                if temp==s1:
                    return True
                else:
                    return False
        