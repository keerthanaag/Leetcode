class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        min_val = min(start,destination)
        max_val = max(start,destination)
        return min(sum(distance[min_val:max_val]),sum(distance[max_val:])+sum(distance[:min_val]))
        