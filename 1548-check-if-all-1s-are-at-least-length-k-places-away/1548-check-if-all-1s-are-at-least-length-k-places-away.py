class Solution(object):
    def kLengthApart(self, nums, k):
        pos = -1
        for i in range(0,len(nums)):
            if nums[i] == 1:
                if pos == -1:
                    pos = i
                else:
                    if (i-pos-1) < k:
                        return False
                    else:
                        pos = i
        return True
        