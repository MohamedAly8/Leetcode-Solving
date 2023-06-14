class Solution:
    def numDecodings(self, s: str) -> int:

        dp = { len(s) : 1 }


        def dfs(i):

            # already been cached or last position
            if i in dp:
                return dp[i]
            
            # no way to decode
            if s[i] == "0":
                return 0
            
            # now it is 1-9, can be taken as single digit
            res = dfs(i+1)

            # there is 2nd character and the 2 numbers are 10-26
            if (i + 1 < len(s) and ((s[i] == "1") or (s[i] == "2" and s[i+1] in "0123456"))):
                res += dfs(i+2)
            
            dp[i] = res

            return res
        
        return dfs(0)


