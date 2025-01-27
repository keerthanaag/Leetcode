class Solution(object):
    def minimumOperations(self, nums):
        cnt = 0
        while len(nums) != len(set(nums)):
            if len(nums) == 3:
                return cnt+1
            nums = nums[3:]
            cnt +=1
        return cnt  