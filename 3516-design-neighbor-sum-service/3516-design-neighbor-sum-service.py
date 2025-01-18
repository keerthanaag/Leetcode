class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def adjacentSum(self, value: int) -> int:
        for i in range(len(self.grid)):
            print(self.grid[i])
            for j in range(len(self.grid[i])):
                out = len(self.grid[i])
                if self.grid[i][j]== value:
                    x = i
                    y = j
                    break
        ans = 0
        if y+1 != out:
            ans += self.grid[x][y+1]
        if y-1 != -1:
            ans += self.grid[x][y-1]
        if x+1 != out:
            ans += self.grid[x+1][y]
        if x-1 != -1:
            ans += self.grid[x-1][y]
        return ans

    def diagonalSum(self, value: int) -> int:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                out = len(self.grid[i])
                if self.grid[i][j]== value:
                    x = i
                    y = j
                    break
        ans = 0
        #DIAG
        if  x-1 != -1 and y+1 != out:
            ans += self.grid[x-1][y+1]
        if x+1 != out and y-1 != -1:
            ans += self.grid[x+1][y - 1]
        if y+1 != out and x+1 != out:
            ans += self.grid[x+1][y+1]
        if x-1 != -1 and y-1 != -1:
            ans += self.grid[x-1][y-1]
        return ans


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)