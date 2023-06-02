class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):

            if ( r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c] == "0"):
                return  

            visit.add((r,c))

            dfs(r+1, c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)
                
        return islands
            









