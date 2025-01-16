class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i] >=k:
                return i
        