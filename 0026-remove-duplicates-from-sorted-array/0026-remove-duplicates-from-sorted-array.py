class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lst = []
        i = 0
        while i < len(nums):
            if nums[i] not in lst:
                lst.append(nums[i])
                i +=1
            else:
                nums.pop(i)
        return len(nums)
        