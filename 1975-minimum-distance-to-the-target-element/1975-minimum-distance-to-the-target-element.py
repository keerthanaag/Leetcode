class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        dist = -1
        for i in range(len(nums)):
            if target == nums[i]:
                temp = abs(i-start)
                if dist == -1 or dist > temp:
                    dist = temp
        return dist
        