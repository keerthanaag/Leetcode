class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0 
        elif len(set(nums)) == len(nums):
            return len(nums)-2
        else:
            nums.sort()
            first = nums[0]
            last = nums[len(nums)-1]
            for i in range(0,len(nums)):
                if nums[i] == first:
                    posf = i
                if nums[i] != last:
                    posl = i
            return posl-posf 
        