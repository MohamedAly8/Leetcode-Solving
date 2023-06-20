class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        dp = [[0 for _ in range(n)] for _ in range(m)]


        # initialize last row and last col
        for i in range(n):
            dp[m-1][i] = 1
        
        for i in range(m):
            dp[i][n-1] = 1

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]