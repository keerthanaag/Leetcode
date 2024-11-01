class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # n=len(s)
        # i=0
        # while i< n-2:
        #     print(i,n,s)
        #     print(s[i],s[i+1],s[i+2])
        #     if s[i]==s[i+1] and s[i]==s[i+2]:
        #         s=s[:i]+s[i+1:]
        #         i-=1
        #     i+=1
        #     n=len(s)
        # return s
        if len(s) < 3:
            return s
        
        # Initialize a list to build the result efficiently
        result = [s[0], s[1]]
        
        for i in range(2, len(s)):
            # Only add the current character if it doesn't form a triple with the last two characters
            if not (s[i] == s[i-1] == s[i-2]):
                result.append(s[i])
        
        # Convert the list back to a string
        return ''.join(result)
        

        