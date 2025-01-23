class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = [row.count(1) for row in grid]
        col = [sum(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (row[i] > 1 or col[j] > 1):
                    c += 1
        print(c)
        return c
        