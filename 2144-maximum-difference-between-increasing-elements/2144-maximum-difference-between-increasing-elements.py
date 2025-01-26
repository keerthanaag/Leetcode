class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff = -1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j] and nums[j] - nums[i] > diff:
                    diff = nums[j] - nums[i]
        return diff
        