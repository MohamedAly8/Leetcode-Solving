class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]
        curMin, curMax = 1, 1

        # maintain maximuum and minimum as you go


        for num in nums:
            tmp = curMax * num
            curMax = max(curMax * num, curMin*num, num)
            curMin = min(tmp, curMin*num, num)
            res = max(curMax, res)
        
        return res
