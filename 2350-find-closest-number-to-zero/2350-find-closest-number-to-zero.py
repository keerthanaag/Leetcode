class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.append(0)
        nums.sort()
        pos = nums.index(0)
        print(nums,pos)
        if len(nums) - 1 == pos:
            return nums[pos-1]
        elif pos == 0:
            return nums[1]
        else:
            if abs(nums[pos-1])<nums[pos+1]:
                return nums[pos-1]
            return nums[pos+1]
        