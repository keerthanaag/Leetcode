class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            temp = []
            for i in range(len(nums)//2):
                if i %2 == 0:
                    temp.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    temp.append(max(nums[2 * i], nums[2 * i + 1]))
            print(nums,temp)
            nums = temp
        print(nums)
        return nums[0]
        while len(nums) > 1:
            temp = [0]*(len(nums)//2)
            for i in range(len(temp)):
                if i %2 == 0:
                    temp[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    temp[i] = max(nums[2 * i], nums[2 * i + 1])
            nums = temp
        return nums[0]