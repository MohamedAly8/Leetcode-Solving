class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1


        # heuristic, 
        # move away when at negative


        # sell when the next transaction results in a decrease of profit

        res = 0

        for i in range(1, len(prices)):
            cur = prices[i]-prices[i-1]
            if cur > 0:
                res += cur

        return res 




