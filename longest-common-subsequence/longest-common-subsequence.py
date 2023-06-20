class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        mx = 0

        n = len(text1); m = len(text2)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
    
                if text1[j] == text2[i]:

                    if i > 0 and j > 0:
                        dp[i][j] = 1 + dp[i-1][j-1]
                        
                    else:
                        dp[i][j] = 1
                        
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                
        print(dp)
        return dp[-1][-1]