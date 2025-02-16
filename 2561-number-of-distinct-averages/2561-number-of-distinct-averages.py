class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        lst = set({})
        i = 0
        while len(nums) != 0:
            avg = (nums[0] + nums[len(nums)-1])/2
            lst.add(avg)
            nums.pop(0)
            nums.pop(len(nums)-1)
        return len(lst)
        