class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mp = 0

        l = 0 
        r = 1

        while r < len(prices):


            cur = prices[r] - prices[l]
            if cur >= 0:
                mp = max(cur, mp) 
                r += 1
            else:
                l = r 
                r += 1
            

        return mp

            

            

            


        

