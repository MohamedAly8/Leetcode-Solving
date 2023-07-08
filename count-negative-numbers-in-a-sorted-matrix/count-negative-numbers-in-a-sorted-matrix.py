class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS = len(grid)
        COLS = len(grid[0])

        r = 0
        c = len(grid[0]) - 1

        nonNegIndex = len(grid[0])
        res = 0

        while r < ROWS:

    
            for c in range(nonNegIndex-1,-1,-1):
                if grid[r][c] >= 0:
                    nonNegIndex = c + 1
                    break
            else:
                nonNegIndex = 0

            res += COLS - nonNegIndex
            r += 1
    
        return res
                







        