class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # d={'I':1,'V' :5,'X' :10,'L':50,'C':100,'D':500,'M' :1000}
        # i=0
        # ans=0
        # while i<len(s):
        #     print(i,s[i],ans)
        #     if s[i]==u'I':
        #         if i+1 < len(s):
        #             if s[i+1]== 'V' or s[i+1]=='X' :
        #                 ans+=d.get(s[i+1])-1
        #                 i+=1
        #         else:
        #             ans+=d.get(s[i])
        #     elif s[i]== 'X':
        #         if i+1 < len(s):
        #             if s[i+1]== 'L' or s[i+1]=='C':
        #                 ans+=d.get(s[i+1])-10
        #                 i+=1
        #         else:
        #             ans+=d.get(s[i])
        #     elif s[i]=='C':
        #         if i+1 < len(s):
        #             if s[i+1]== 'D' or s[i+1]=='M':
        #                 ans+=d.get(s[i+1])-100
        #                 i+=1
        #         else:
        #             ans+=d.get(s[i])
        #     else:
        #         ans+=d.get(s[i])
        #     i+=1
        # return ans
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        ans = 0
        while i < len(s):
            if i + 1 < len(s) and d[s[i]] < d[s[i + 1]]:
                # Special case: subtract the current value from the next one (e.g., IV, IX, etc.)
                ans += d[s[i + 1]] - d[s[i]]
                i += 2
            else:
                ans += d[s[i]]
                i += 1
        return ans

                    
            
        