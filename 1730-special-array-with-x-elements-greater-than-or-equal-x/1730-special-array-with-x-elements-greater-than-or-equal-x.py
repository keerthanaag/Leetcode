class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        elif len(nums) == 1 and nums[0] != 0:
            return 1
        else:
            for x in range(2,len(nums)+1):
                pos=-1
                for y in range(0,len(nums)):
                    if nums[y] >= x:
                        pos = y
                        break
                if pos != -1 and x == len(nums[pos:]):
                    return x
        return -1


        