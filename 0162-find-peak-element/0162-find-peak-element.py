class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))
        max_element = nums[0]
        index = 0
        for i in range(1,len(nums)):
            if nums[i] > max_element:
                max_element = nums[i]
                index = i
        return index
        