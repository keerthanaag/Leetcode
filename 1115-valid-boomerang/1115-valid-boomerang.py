class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        x0, y0 = points[0]
        x1, y1 = points[1]
        dx, dy = x1 - x0, y1 - y0
        x, y = points[2]
        if (y - y0) * dx == (x - x0) * dy:
            return False
        return True
        