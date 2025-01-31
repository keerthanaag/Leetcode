class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        min_val = min(start,destination)
        max_val = max(start,destination)
        print(distance[min_val:max_val],sum(distance[min_val:max_val]))
        print(distance[max_val:],distance[:min_val],sum(distance[max_val:])+sum(distance[:min_val]))
        return min(sum(distance[min_val:max_val]),sum(distance[max_val:])+sum(distance[:min_val]))