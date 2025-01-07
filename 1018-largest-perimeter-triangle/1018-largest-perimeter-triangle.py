class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        perimeter = 0 
        nums.sort(reverse = True)
        for i in range(len(nums)-2):
            print(nums[i:i+3])
            if nums[i] < nums[i+1] + nums[i+2]:
                print(sum(nums[i:i+3]))
                return sum(nums[i:i+3])
        return perimeter

        