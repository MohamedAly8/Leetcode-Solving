class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]
        curMin, curMax = 1, 1

        # maintain maximuum and minimum as you go


        for num in nums:
            
            cur = curMax * num

            curMax = max(cur, curMin*num, num)
            curMin = min(cur, curMin*num, num)
            res = max(curMax, res)
        
        return res
