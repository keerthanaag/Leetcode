class Solution(object):
    def getMinDistance(self, nums, target, start):
        dist = -1
        for i in range(len(nums)):
            if target == nums[i]:
                temp = abs(i-start)
                if dist == -1 or dist > temp:
                    dist = temp
        return dist   