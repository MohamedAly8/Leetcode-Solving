class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS,COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        

        def dfs(r,c,visited,prevHeight):

            if (r not in range(ROWS) or 
                c not in range(COLS) or 
                (r,c) in visited     or 
                prevHeight > heights[r][c]):

                return 
            
            # we gud
            visited.add((r,c))

            # dfs around it
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])


        # visit all elements on first row and last row
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])

        # visit all elements on first and last column
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res
        
 






