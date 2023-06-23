class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1


        # heuristic, 
        # move away when at negative


        # sell when the next transaction results in a decrease of profit

        res = 0

        while r < len(prices):

            profit = prices[r] - prices[l]
            # losing money, move on 
            if prices[r] - prices[l] < 0:
                l = r
                r += 1
            # if increasing one more day makes profit less, sell
            elif r < len(prices) - 1 and profit > prices[r+1] - prices[l]:
                res += profit
                l = r
                r += 1       
            else:
                r += 1
            if profit > 0 and r == len(prices):
                res += profit

        return res



