class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxi = min(rectangles[0])
        print(maxi)
        count = 0 
        for x in rectangles:
            val = min(x)
            #print(val)
            if maxi == val:
                count += 1
            elif maxi < val:
                maxi = val
                count = 1
        return count 

        