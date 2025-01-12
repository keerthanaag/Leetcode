class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxi = min(rectangles[0])
        count = 0 
        for x in rectangles:
            if maxi == min(x):
                count += 1
            elif maxi < min(x):
                maxi = min(x)
                count = 1
        return count 

        