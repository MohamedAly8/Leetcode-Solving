class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mp = 0

        l = 0 
        r = 1

        while r < len(prices):


            cur = prices[r] - prices[l]

            # we in the negatives
            if cur >= 0:
                mp = max(cur, mp) 
                r += 1

            elif cur < 0:
                l += 1
                if not l < r:
                    r += 1
            

        return mp

            

            

            


        

