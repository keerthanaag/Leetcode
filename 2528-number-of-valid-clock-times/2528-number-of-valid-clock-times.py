class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        ans=1
        if time[4]=='?':
            if time[3] == '6':
                ans=1
            elif time[3] == '?':
                ans*=60
            else:
                ans*= 10
        if time[3] == '?' and time[4] != '?':
            ans*=6
        if time[1] =='?':
            if time[0] == '2':
                ans *= 4
            elif time[0] == '?':
                ans *= 24
            else:
                ans *= 10
        if time[0] == '?' and time[1] != '?':
            if int(time[1]) <= 3:
                ans*= 3
            else:
                ans *= 2
        return ans

        