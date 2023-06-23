class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # For every index in s
        dp = [False] * (len(s)+1)

        #Base case, at the very end 
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):

            for w in wordDict:
                # comparing 
                if (i+len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]

                if dp[i]:
                    break
        
        return dp[0]


