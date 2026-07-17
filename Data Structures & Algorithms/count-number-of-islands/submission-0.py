class Solution:

    def startdfs(self, row, col, grid: List[List[str]]):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return
        
        if grid[row][col] == "0" or self.visited[row][col] == 1:
            return

        self.visited[row][col] = 1

        self.startdfs(row + 1, col, grid)
        self.startdfs(row - 1, col, grid)
        self.startdfs(row, col + 1, grid)
        self.startdfs(row, col - 1, grid)


    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])

        self.visited = [[0] * self.cols for _ in range(self.rows)]
        islands = 0

        for i, row in enumerate(grid):
            for col in range(len(grid[0])):
                if row[col] == "1" and not self.visited[i][col]:
                    self.startdfs(i, col, grid)
                    islands += 1

        return islands