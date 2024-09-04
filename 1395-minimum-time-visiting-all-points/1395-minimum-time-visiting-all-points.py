class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(1, len(points)):
            start = points[i - 1]
            des = points[i]
            count += max(abs(des[0] - start[0]), abs(des[1] - start[1]))
        return count