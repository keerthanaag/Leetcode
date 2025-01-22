class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist = -1
        index = -1     
        for i,pt in enumerate(points):
            if x == pt[0] or y == pt[1]:
                temp = abs(x-pt[0]) + abs(y-pt[1])
                if dist == -1 or dist > temp:
                    dist = temp
                    index = i
        return index
