class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:

            cur = curMax * num
            curMax = max(cur, num*curMin, num)
            curMin = min(cur, num*curMin, num)

            res = max(res, curMax)
        
        return res
