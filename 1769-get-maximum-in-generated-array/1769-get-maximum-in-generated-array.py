class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0] * (n+1) 
        nums[0] = 0
        if n > 0:
            nums[1] = 1
        for i in range(1,n):
            flag = 0
            if (2 <= 2 * i) and (2 * i <= n):
                nums[2 * i] = nums[i]
                flag = 1
            if (2 <= 2 * i + 1) and (2 * i + 1 <= n):
                nums[2 * i + 1] = nums[i] + nums[i + 1]
                flag = 1
            if flag == 0:
                break
        return max(nums)
        