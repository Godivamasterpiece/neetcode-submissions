class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        self.rows = len(grid)
        self.cols = len(grid[0])

        from collections import deque

        dq = deque()
        fresh = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 2:
                    dq.append((row,col, 0))
                elif grid[row][col] == 1:
                    fresh += 1

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        mins = 0

        while dq:
            r, c, current_min = dq.popleft()

            for dr,dc in directions:
                nr, nc = r+ dr, c + dc

                if( 0<= nr < self.rows and 0<= nc < self.cols and grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    fresh -= 1
                    dq.append((nr,nc, current_min + 1))
                    mins = max(mins, current_min + 1)

        return mins if fresh == 0 else -1