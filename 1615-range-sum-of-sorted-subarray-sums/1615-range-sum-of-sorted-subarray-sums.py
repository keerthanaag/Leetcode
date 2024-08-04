class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        lst=[]
        for i in range(0,len(nums)):
            temp=0
            for j in range(i,len(nums)):
                temp+=nums[j]
                lst.append(temp)
        lst=sorted(lst)
        mod = 10**9 + 7
        return sum(lst[left-1:right]) % mod