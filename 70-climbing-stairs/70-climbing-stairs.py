class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        if n <= 3:
            return n

        dp = [1 for i in range(n+1)]

        for i in range(n-2,-1,-1):
            dp[i] = dp[i+1] + dp[i+2]      
        
        return dp[0]