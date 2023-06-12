class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(nums):

            h1, h2 = 0,0
            for i in range(len(nums)):
                temp = h1 + nums[i]
                h1 = h2
                h2 = max(temp, h1)
            return h2

        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))




