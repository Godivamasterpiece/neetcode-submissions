class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.rows = len(heights)
        self.cols = len(heights[0])

        visited_pac = set()
        visited_atl = set()

        def dfs(r, c, visit_set, prev_height):
            if (r<0 or r >= self.rows or c<0 or c >= self.cols or (r,c) in visit_set or heights[r][c] < prev_height):
                return
            visit_set.add((r,c))

            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            for dr, dc in directions:
                dfs(r+dr,c+dc,visit_set,heights[r][c])

        for col in range(self.cols):
            dfs(0,col, visited_pac, heights[0][col])
            dfs(self.rows-1, col, visited_atl, heights[self.rows-1][col])

        for row in range(self.rows):
            dfs(row,0, visited_pac, heights[row][0])
            dfs(row,self.cols-1, visited_atl, heights[row][self.cols-1])

        results = []
        for r in range(self.rows):
            for c in range(self.cols):
                if(r,c) in visited_pac and (r,c) in visited_atl:
                    results.append([r,c])

        return results

        

        

