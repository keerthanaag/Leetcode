class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        s=sorted(score,reverse=True)
        lst=[]
        for x in score:
            for i in range(len(s)):
                if x==s[i]:
                    if i==0:
                        lst.append("Gold Medal")
                    elif i==1:
                        lst.append("Silver Medal")
                    elif i==2:
                        lst.append("Bronze Medal")
                    else:
                        lst.append(str(i+1))
                    break
        return lst
        