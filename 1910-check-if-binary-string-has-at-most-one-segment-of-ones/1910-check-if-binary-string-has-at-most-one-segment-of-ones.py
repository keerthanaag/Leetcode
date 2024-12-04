class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x = re.sub("0+", " ", s)
        ans = x.strip().split(" ")
        print(ans)
        if len(ans) >=2:
            return False
        return True
        