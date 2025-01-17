class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sums = 0
        temp = 0
        for i in range(0,len(nums)):
            print(temp,nums[i],nums[i-1])
            if i == 0 or nums[i] > nums[i-1]:
                temp += nums[i]
            else:
                sums = max(sums,temp)
                temp = nums[i]
        return max(sums,temp)
        