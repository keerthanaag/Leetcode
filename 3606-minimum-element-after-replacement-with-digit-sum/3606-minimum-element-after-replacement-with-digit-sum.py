class Solution:
    def minElement(self, nums: List[int]) -> int:
        val=max(nums)
        for num in nums:
            digit=0
            while num !=0:
                digit+=num%10
                num=num//10
            print(digit)
            val=min(val,digit)
        return val
        