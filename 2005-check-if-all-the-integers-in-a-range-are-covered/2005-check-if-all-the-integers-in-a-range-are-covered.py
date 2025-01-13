class Solution(object):
    def isCovered(self, ranges, left, right):
        val = left
        ranges.sort()
        i=0
        while i < len(ranges):
            if ranges[i][0] <= val <= ranges[i][1]:
                val+=1
            else:
                i+=1
            if val > right:
                return True
        return False
        