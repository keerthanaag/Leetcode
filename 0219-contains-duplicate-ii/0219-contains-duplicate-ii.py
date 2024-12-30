class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}  # Dictionary to store the last seen index of each number
        for i, num in enumerate(nums):
            if num in seen and abs(i - seen[num]) <= k:
                return True
            seen[num] = i  # Update the last seen index
        return False
        

        