class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        f = 0
        l = len(nums)
        mid = len(nums)//2
        if nums[mid] >= k:
            return self.search(nums,k,f,mid+1)
        else:
            return self.search(nums,k,mid+1,l)
    def search(self,nums: List[int], k: int,start: int,end: int):
        for i in range(start,end):
            if nums[i]>= k:
                    return i

            
        