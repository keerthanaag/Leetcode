class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp=nums.pop()
            nums.insert(0,temp)
        # n=len(nums)
        # temp=nums[n-k:]
        # temp.extend(nums[:k])
        # print(temp)
        