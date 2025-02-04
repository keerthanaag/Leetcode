class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count = 0
        temp = 0
        for i in range(0,len(nums)):
            #print(temp,nums[i],nums[i-1])
            if i == 0 or nums[i] > nums[i-1]:
                temp += 1
            else:
                count = max(count,temp)
                temp = 1
        count = max(count,temp)
        print("count: ",count)
        num = nums[::-1]
        print(num,nums)
        temp = 0
        for i in range(0,len(num)):
            print(temp,num[i],num[i-1])
            if i == 0 or num[i] > num[i-1]:
                temp += 1
            else:
                count = max(count,temp)
                temp = 1
        count = max(count,temp)
        print("count: ",count)
        return count