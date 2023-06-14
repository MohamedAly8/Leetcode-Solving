class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #  dp to save min values from 1 -> amount
        dp =  [amount + 1] * (amount + 1)
        dp[0] = 0

        print(dp)
        # start from 1 -> amount
        for a in range(1, amount+1):
            # check if any coins could be added to this
            for coin in coins:
                # potential coin to be used
                if a >= coin:
                    dp[a] = min(dp[a], 1+dp[a-coin])
            
        print(dp)
        return dp[amount] if dp[amount] != amount + 1 else -1



