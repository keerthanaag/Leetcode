class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        val = left
        ranges.sort()
        i=0
        while i < len(ranges):
            if ranges[i][0] <= val <= ranges[i][1]:
                val+=1
                print(val)
            else:
                i+=1
            if val > right:
                return True
        return False
        