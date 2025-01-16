class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        f, l = 0, len(nums)
        mid = l // 2
        pos = self.binarySearch(nums, k, f, mid) if nums[mid] >= k else self.binarySearch(nums, k, mid + 1, l)
        return pos

    def binarySearch(self, nums: List[int], k: int, start: int, end: int) -> int:
        while start < end:
            mid = (start + end) // 2
            if nums[mid] >= k:
                end = mid
            else:
                start = mid + 1
        return start if start < len(nums) and nums[start] >= k else -1


            
        