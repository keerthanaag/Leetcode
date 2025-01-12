class Solution(object):
    def countGoodRectangles(self, rectangles):
        maxi = min(rectangles[0])
        count = 0 
        for x in rectangles:
            val = min(x)
            if maxi == val:
                count += 1
            elif maxi < val:
                maxi = val
                count = 1
        return count 

        