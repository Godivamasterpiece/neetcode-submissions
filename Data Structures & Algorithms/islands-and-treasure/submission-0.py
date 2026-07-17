class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        self.inf = 2147483647

        self.rows = len(grid)
        self.cols = len(grid[0])

        self.visited = [[0] * self.cols for _ in range(self.rows)]

        from collections import deque

        dq = deque()

        for row in range(self.rows):
            for col in range(self.cols):
                
                ## Find all the treasure 
                ## then deque
                if grid[row][col] == 0:
                    dq.append((row,col))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while dq:
            r, c = dq.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if ( 0 <= nr < self.rows and 0 <= nc < self.cols and grid[nr][nc] == self.inf):

                    grid[nr][nc] = grid[r][c] + 1
                    dq.append((nr,nc))



        return