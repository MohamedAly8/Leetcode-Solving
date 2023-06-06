class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS,COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(r,c,visit, prevHeight):
            # if already visited or out of bounds OR IF HEIGHT IS LESS THAT PREVIOUS HEIGHT
            if ((r,c) in visit or 
                r < 0 or c < 0 or r == ROWS or c == COLS or 
                not(heights[r][c] >= prevHeight)):
                return
            
            # add to visited
            visit.add((r,c))

            # DFS all around 
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for c in range(COLS):
            # first & last row
            dfs(0,c,pac, heights[0][c])
            dfs(ROWS-1,c,atl, heights[ROWS-1][c])

        for r in range(ROWS):
            # first & last column
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        
        # check every cell if it is in both Pac & Atl
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
    

        return res




