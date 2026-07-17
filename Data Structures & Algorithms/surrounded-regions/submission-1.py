class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        self.rows = len(board)
        self.cols = len(board[0])

        connected_edges = []

        def dfs(r,c, grid):

            if not (0 <= r <self.rows and 0<=c<self.cols):
                return
            if grid[r][c] != 'O' or (r,c) in connected_edges:
                return

            connected_edges.append((r,c))
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]

            for (dr,dc) in dirs:
                dfs(dr+r,dc+c, grid)


        for r in range(self.rows):
            ## check 0
            if(board[r][0] == 'O'):
                dfs(r,0, board)
            if(board[r][self.cols-1] == 'O'):
                dfs(r,self.cols-1, board)

        for c in range(self.cols):
            if(board[0][c] == 'O'):
                dfs(0,c, board)
            if(board[self.rows-1][c] == 'O'):
                dfs(self.rows-1, c, board)

        for r in range(self.rows):
            for c in range(self.cols):
                if board[r][c] == 'O' and (r,c) not in connected_edges:
                    board[r][c] = 'X'