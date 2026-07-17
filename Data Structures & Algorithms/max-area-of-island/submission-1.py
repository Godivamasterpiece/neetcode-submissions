class Solution:

    def dfs(self, row, col, grid):

        if row < 0 or row >= self.rows or col < 0  or col >= self.cols:
            return 0

        if grid[row][col] == 0 or self.visited[row][col] == 1:
            return 0 

        self.visited[row][col] = 1
       

        return (1 + self.dfs(row - 1, col, grid) + self.dfs(row + 1, col, grid) + self.dfs(row, col - 1 , grid) + self.dfs(row, col + 1, grid))

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        self.rows = len(grid)
        self.cols = len(grid[0])

        self.visited = [[0] * self.cols for _ in range(self.rows)]
        self.maxarea = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1 and not self.visited[row][col]:
                    currArea  = self.dfs(row,col, grid)
                    self.maxarea = max(currArea, self.maxarea)

        return self.maxarea