class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
    
                if text1[i] == text2[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return dp[-1][-1]